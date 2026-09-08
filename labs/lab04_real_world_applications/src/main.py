"""Menu-driven entry point for the Lab 4 applications."""

try:
    from .hospital import HospitalSystem
    from .restaurant import RestaurantSystem
    from .vehicle import VehicleRentalSystem
except ImportError:
    from hospital import HospitalSystem
    from restaurant import RestaurantSystem
    from vehicle import VehicleRentalSystem


def _read_text(prompt: str) -> str:
    return input(prompt).strip()


def _read_int(prompt: str) -> int:
    try:
        return int(_read_text(prompt))
    except ValueError:
        raise ValueError("Invalid numerical input") from None


def _read_float(prompt: str) -> float:
    try:
        return float(_read_text(prompt))
    except ValueError:
        raise ValueError("Invalid numerical input") from None


def _show_error(action, success_message=None):
    try:
        action()
        if success_message:
            print(success_message)
        return True
    except ValueError as error:
        print(f"Error: {error}")
        return False


def _show_patients(system: HospitalSystem):
    patients = system.list_patients()
    if not patients:
        print("No patients found.")
        return
    for patient in patients:
        print(
            f"{patient.patient_id} | {patient.patient_name} | {patient.doctor_name} | "
            f"{patient.department} | {patient.appointment_date or '-'} | "
            f"{patient.appointment_status}"
        )


def run_hospital():
    system = HospitalSystem()
    while True:
        print(
            "\nHospital Appointment Management System\n"
            "1. Add a patient\n2. Display all patients\n3. Search for a patient\n"
            "4. Book an appointment\n5. Cancel an appointment\n"
            "6. Update appointment details\n7. Display appointments for a doctor\n"
            "8. Display appointment report\n9. Exit"
        )
        try:
            choice = _read_int("Enter choice: ")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if choice == 1:
            _show_error(
                lambda: system.add_patient(
                    _read_text("Patient ID: "),
                    _read_text("Patient name: "),
                    _read_text("Doctor name: "),
                    _read_text("Department: "),
                ),
                "Patient added successfully.",
            )
        elif choice == 2:
            _show_patients(system)
        elif choice == 3:
            _show_error(lambda: print(system.search_patient(_read_text("Patient ID: "))))
        elif choice == 4:
            _show_error(
                lambda: system.book_appointment(
                    _read_text("Patient ID: "),
                    _read_text("Doctor name: "),
                    _read_text("Appointment date (YYYY-MM-DD): "),
                ),
                "Appointment booked successfully.",
            )
        elif choice == 5:
            _show_error(
                lambda: system.cancel_appointment(_read_text("Patient ID: ")),
                "Appointment cancelled successfully.",
            )
        elif choice == 6:
            _show_error(
                lambda: system.update_appointment(
                    _read_text("Patient ID: "),
                    _read_text("New doctor name: "),
                    _read_text("New appointment date (YYYY-MM-DD): "),
                ),
                "Appointment updated successfully.",
            )
        elif choice == 7:
            _show_error(
                lambda: [print(patient) for patient in system.appointments_for_doctor(
                    _read_text("Doctor name: ")
                )]
            )
        elif choice == 8:
            print(system.appointment_report())
        elif choice == 9:
            print("Exiting hospital application.")
            return
        else:
            print("Invalid menu choice")


def _show_food_items(system: RestaurantSystem):
    items = system.list_food_items()
    if not items:
        print("No food items found.")
        return
    for item in items:
        print(
            f"{item.food_id} | {item.food_name} | {item.category} | "
            f"{item.price:.2f} | stock={item.available_quantity}"
        )


def _print_bill(system: RestaurantSystem):
    bill = system.calculate_bill()
    print(f"Subtotal: {bill.subtotal:.2f}")
    print(f"Discount: {bill.discount:.2f}")
    print(f"Final total: {bill.total:.2f}")


def run_restaurant():
    system = RestaurantSystem()
    while True:
        print(
            "\nRestaurant Order Management System\n"
            "1. Add a food item\n2. Display all food items\n3. Search for a food item\n"
            "4. Add a food item to an order\n5. Remove a food item from an order\n"
            "6. Update food quantity\n7. Display the customer order\n8. Calculate the bill\n"
            "9. Apply discount\n10. Generate final bill\n11. Exit"
        )
        try:
            choice = _read_int("Enter choice: ")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if choice == 1:
            _show_error(
                lambda: system.add_food_item(
                    _read_text("Food ID: "),
                    _read_text("Food name: "),
                    _read_text("Category: "),
                    _read_text("Price: "),
                    _read_int("Available quantity: "),
                ),
                "Food item added successfully.",
            )
        elif choice == 2:
            _show_food_items(system)
        elif choice == 3:
            _show_error(lambda: print(system.search_food_item(_read_text("Food ID: "))))
        elif choice == 4:
            _show_error(
                lambda: system.add_to_order(
                    _read_text("Food ID: "), _read_int("Quantity: ")
                ),
                "Food item added to order.",
            )
        elif choice == 5:
            _show_error(
                lambda: system.remove_from_order(_read_text("Food ID: ")),
                "Food item removed from order.",
            )
        elif choice == 6:
            _show_error(
                lambda: system.update_quantity(
                    _read_text("Food ID: "), _read_int("New quantity: ")
                ),
                "Food quantity updated.",
            )
        elif choice == 7:
            _show_error(
                lambda: [print(f"{item.food_name}: {quantity}") for item, quantity in system.order_items()]
            )
        elif choice == 8:
            _show_error(lambda: _print_bill(system))
        elif choice == 9:
            _show_error(lambda: print(f"Discount applied: {system.calculate_bill().discount:.2f}"))
        elif choice == 10:
            _show_error(lambda: _print_bill(system))
        elif choice == 11:
            print("Exiting restaurant application.")
            return
        else:
            print("Invalid menu choice")


def _show_vehicles(vehicles):
    if not vehicles:
        print("No vehicles found.")
        return
    for vehicle in vehicles:
        status = "Available" if vehicle.is_available else "Rented"
        print(
            f"{vehicle.vehicle_id} | {vehicle.vehicle_name} | {vehicle.vehicle_type} | "
            f"{vehicle.rental_price_per_day:.2f}/day | {status}"
        )


def run_vehicle_rental():
    system = VehicleRentalSystem()
    while True:
        print(
            "\nVehicle Rental Management System\n"
            "1. Add a vehicle\n2. Display all vehicles\n3. Search for a vehicle\n"
            "4. Rent a vehicle\n5. Return a vehicle\n6. Display available vehicles\n"
            "7. Display rented vehicles\n8. Exit"
        )
        try:
            choice = _read_int("Enter choice: ")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if choice == 1:
            _show_error(
                lambda: system.add_vehicle(
                    _read_text("Vehicle ID: "),
                    _read_text("Vehicle name: "),
                    _read_text("Vehicle type: "),
                    _read_float("Rental price per day: "),
                ),
                "Vehicle added successfully.",
            )
        elif choice == 2:
            _show_vehicles(system.list_vehicles())
        elif choice == 3:
            _show_error(lambda: print(system.search_vehicle(_read_text("Vehicle ID: "))))
        elif choice == 4:
            _show_error(
                lambda: system.rent_vehicle(_read_text("Vehicle ID: ")),
                "Vehicle rented successfully.",
            )
        elif choice == 5:
            _show_error(
                lambda: system.return_vehicle(_read_text("Vehicle ID: ")),
                "Vehicle returned successfully.",
            )
        elif choice == 6:
            _show_vehicles(system.available_vehicles())
        elif choice == 7:
            _show_vehicles(system.rented_vehicles())
        elif choice == 8:
            print("Exiting vehicle rental application.")
            return
        else:
            print("Invalid menu choice")


def main():
    while True:
        print(
            "\nSoftware Engineering Lab 4\n"
            "1. Hospital Appointment Management System\n"
            "2. Restaurant Order Management System\n"
            "3. Vehicle Rental Management System\n"
            "4. Exit"
        )
        try:
            choice = _read_int("Select application: ")
        except ValueError as error:
            print(f"Error: {error}")
            continue
        if choice == 1:
            run_hospital()
        elif choice == 2:
            run_restaurant()
        elif choice == 3:
            run_vehicle_rental()
        elif choice == 4:
            print("Goodbye")
            return
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()
