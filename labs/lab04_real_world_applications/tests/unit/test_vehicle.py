import pytest

from labs.lab04_real_world_applications.src.vehicle import VehicleRentalSystem


def vehicle(system, vehicle_id="V001"):
    system.add_vehicle(vehicle_id, "Swift Dzire", "Sedan", "1800")


def test_add_search_and_duplicate_vehicle():
    system = VehicleRentalSystem()
    added = system.add_vehicle("V001", "Swift Dzire", "Sedan", "1800")

    assert added.vehicle_name == "Swift Dzire"
    assert system.search_vehicle("V001").rental_price_per_day == 1800.0
    with pytest.raises(ValueError, match="Duplicate vehicle ID"):
        vehicle(system)


def test_rent_and_return_validate_vehicle_state():
    system = VehicleRentalSystem()
    vehicle(system)
    system.rent_vehicle("V001")
    assert len(system.rented_vehicles()) == 1

    with pytest.raises(ValueError, match="already rented"):
        system.rent_vehicle("V001")

    system.return_vehicle("V001")
    assert len(system.available_vehicles()) == 1
    with pytest.raises(ValueError, match="already available"):
        system.return_vehicle("V001")


@pytest.mark.parametrize("price", ["-10", "abc"])
def test_invalid_rental_price_is_rejected(price):
    with pytest.raises(ValueError, match="Rental price"):
        VehicleRentalSystem().add_vehicle("V001", "Swift Dzire", "Sedan", price)


def test_missing_vehicle_is_rejected():
    with pytest.raises(ValueError, match="Vehicle not found"):
        VehicleRentalSystem().rent_vehicle("V404")
