"""Vehicle rental management domain logic and console application."""

from dataclasses import dataclass


@dataclass
class Vehicle:
    vehicle_id: str
    vehicle_name: str
    vehicle_type: str
    rental_price_per_day: float
    is_available: bool = True


def _text(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()


def _rental_price(value) -> float:
    try:
        price = float(value)
    except (TypeError, ValueError):
        raise ValueError("Rental price must be a non-negative number") from None
    if price < 0:
        raise ValueError("Rental price must be a non-negative number")
    return price


class VehicleRentalSystem:
    """In-memory vehicle catalogue with rental state."""

    def __init__(self):
        self._vehicles: dict[str, Vehicle] = {}

    def add_vehicle(self, vehicle_id, vehicle_name, vehicle_type, rental_price_per_day):
        vehicle_id = _text(vehicle_id, "Vehicle ID")
        if vehicle_id in self._vehicles:
            raise ValueError("Duplicate vehicle ID")
        vehicle = Vehicle(
            vehicle_id,
            _text(vehicle_name, "Vehicle name"),
            _text(vehicle_type, "Vehicle type"),
            _rental_price(rental_price_per_day),
        )
        self._vehicles[vehicle_id] = vehicle
        return vehicle

    def list_vehicles(self) -> list[Vehicle]:
        return list(self._vehicles.values())

    def search_vehicle(self, vehicle_id: str) -> Vehicle:
        try:
            return self._vehicles[vehicle_id.strip()]
        except (AttributeError, KeyError):
            raise ValueError("Vehicle not found") from None

    def rent_vehicle(self, vehicle_id: str):
        vehicle = self.search_vehicle(vehicle_id)
        if not vehicle.is_available:
            raise ValueError("Vehicle is already rented")
        vehicle.is_available = False
        return vehicle

    def return_vehicle(self, vehicle_id: str):
        vehicle = self.search_vehicle(vehicle_id)
        if vehicle.is_available:
            raise ValueError("Vehicle is already available")
        vehicle.is_available = True
        return vehicle

    def available_vehicles(self) -> list[Vehicle]:
        return [vehicle for vehicle in self._vehicles.values() if vehicle.is_available]

    def rented_vehicles(self) -> list[Vehicle]:
        return [vehicle for vehicle in self._vehicles.values() if not vehicle.is_available]
