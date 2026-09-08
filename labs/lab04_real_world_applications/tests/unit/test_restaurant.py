from decimal import Decimal

import pytest

from labs.lab04_real_world_applications.src.restaurant import RestaurantSystem


def menu(system, food_id="F001", stock=5):
    system.add_food_item(food_id, "Veg Thali", "Main Course", "250", stock)


def test_add_search_and_duplicate_food_item():
    system = RestaurantSystem()
    item = system.add_food_item("F001", "Veg Thali", "Main Course", "250", 5)

    assert item.food_name == "Veg Thali"
    assert system.search_food_item("F001").price == Decimal("250")
    with pytest.raises(ValueError, match="Duplicate food ID"):
        menu(system)


@pytest.mark.parametrize("price", ["-1", "free", "0"])
def test_invalid_price_is_rejected(price):
    with pytest.raises(ValueError, match="Price must be greater than zero"):
        RestaurantSystem().add_food_item("F001", "Tea", "Beverage", price, 5)


def test_order_rejects_invalid_and_over_stock_quantities():
    system = RestaurantSystem()
    menu(system, stock=2)

    with pytest.raises(ValueError, match="Quantity must be positive"):
        system.add_to_order("F001", 0)
    with pytest.raises(ValueError, match="greater than available stock"):
        system.add_to_order("F001", 3)

    system.add_to_order("F001", 2)
    bill = system.calculate_bill()
    assert bill.subtotal == Decimal("500")
    assert bill.discount == Decimal("0")
    assert bill.total == Decimal("500")


def test_bill_applies_discount_and_empty_order_is_rejected():
    system = RestaurantSystem()
    menu(system, stock=10)
    system.add_to_order("F001", 5)

    bill = system.generate_final_bill()

    assert bill.discount == Decimal("125.00")
    assert bill.total == Decimal("1125.00")
    system.remove_from_order("F001")
    with pytest.raises(ValueError, match="Order is empty"):
        system.calculate_bill()

