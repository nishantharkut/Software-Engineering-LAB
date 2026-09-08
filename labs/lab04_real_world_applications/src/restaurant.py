"""Restaurant order management domain logic and console application."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass
class FoodItem:
    food_id: str
    food_name: str
    category: str
    price: Decimal
    available_quantity: int


@dataclass(frozen=True)
class Bill:
    subtotal: Decimal
    discount: Decimal
    total: Decimal


def _text(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()


def _price(value) -> Decimal:
    try:
        price = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError("Price must be greater than zero") from None
    if price <= 0:
        raise ValueError("Price must be greater than zero")
    return price.quantize(Decimal("0.01"))


def _quantity(value, *, allow_zero=False) -> int:
    try:
        if isinstance(value, bool):
            raise ValueError
        quantity = int(value)
        if str(value).strip() != str(quantity):
            raise ValueError
    except (AttributeError, TypeError, ValueError):
        raise ValueError("Invalid food quantity") from None
    if quantity < 0 or (quantity == 0 and not allow_zero):
        raise ValueError("Quantity must be positive")
    return quantity


class RestaurantSystem:
    """In-memory food catalogue and customer order."""

    def __init__(self):
        self._items: dict[str, FoodItem] = {}
        self._order: dict[str, int] = {}

    def add_food_item(self, food_id, food_name, category, price, available_quantity):
        food_id = _text(food_id, "Food ID")
        if food_id in self._items:
            raise ValueError("Duplicate food ID")
        quantity = _quantity(available_quantity, allow_zero=True)
        item = FoodItem(
            food_id,
            _text(food_name, "Food name"),
            _text(category, "Category"),
            _price(price),
            quantity,
        )
        self._items[food_id] = item
        return item

    def list_food_items(self) -> list[FoodItem]:
        return list(self._items.values())

    def search_food_item(self, food_id: str) -> FoodItem:
        try:
            return self._items[food_id.strip()]
        except (AttributeError, KeyError):
            raise ValueError("Food item not found") from None

    def add_to_order(self, food_id: str, quantity: int):
        item = self.search_food_item(food_id)
        quantity = _quantity(quantity)
        new_quantity = self._order.get(item.food_id, 0) + quantity
        if new_quantity > item.available_quantity:
            raise ValueError("Quantity greater than available stock")
        self._order[item.food_id] = new_quantity

    def remove_from_order(self, food_id: str):
        self.search_food_item(food_id)
        if food_id not in self._order:
            raise ValueError("Food item is not in the order")
        del self._order[food_id]

    def update_quantity(self, food_id: str, quantity: int):
        item = self.search_food_item(food_id)
        quantity = _quantity(quantity, allow_zero=True)
        if quantity > item.available_quantity:
            raise ValueError("Quantity greater than available stock")
        if quantity == 0:
            self._order.pop(item.food_id, None)
        else:
            self._order[item.food_id] = quantity

    def order_items(self) -> list[tuple[FoodItem, int]]:
        return [(self._items[food_id], quantity) for food_id, quantity in self._order.items()]

    def calculate_bill(self) -> Bill:
        if not self._order:
            raise ValueError("Order is empty")
        subtotal = sum(
            (item.price * quantity for item, quantity in self.order_items()),
            Decimal("0.00"),
        ).quantize(Decimal("0.01"))
        discount_rate = Decimal("0.10") if subtotal >= 1000 else Decimal("0.00")
        discount = (subtotal * discount_rate).quantize(Decimal("0.01"))
        return Bill(subtotal, discount, subtotal - discount)

    def generate_final_bill(self) -> Bill:
        return self.calculate_bill()
