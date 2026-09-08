# Lab 4: Real-World Software Applications

## Aim

Design, implement, and test menu-driven console applications using input
validation, error handling, and test-driven development.

This lab implements all three tasks from the Lab Sheet 4 dated 21 August 2026:

1. Hospital Appointment Management System
2. Restaurant Order Management System
3. Vehicle Rental Management System

## Project structure

```text
lab04_real_world_applications/
|-- src/
|   |-- hospital.py       # Patient and appointment domain logic
|   |-- restaurant.py     # Food catalogue, order, and bill logic
|   |-- vehicle.py        # Vehicle catalogue and rental logic
|   `-- main.py           # Menu-driven console entry point
|-- tests/
|   |-- unit/             # Domain validation and operation tests
|   `-- integration/      # Console menu tests
|-- data/
|   |-- input/            # Representative JSON input records
|   `-- output/           # Verified run output and final bill
|-- docs/
|   |-- screenshots/      # Console execution screenshots
|   |-- test_specification.md
|   |-- test_execution_report.md
|   `-- submission_checklist.md
`-- README.md
```

## Run the application

From the repository root:

```powershell
.\.venv\Scripts\python.exe -m labs.lab04_real_world_applications.src.main
```

The top-level menu lets you select one of the three systems. Each system then
provides every operation required by the assignment sheet and remains in its
own menu until the user selects Exit.

## Run tests

```powershell
.\.venv\Scripts\python.exe -m pytest .\labs\lab04_real_world_applications\tests -v
```

The test suite covers valid operations, duplicate and missing IDs, empty text,
invalid dates, invalid numerical values, stock limits, empty orders, rental
state transitions, and invalid menu choices.

## Business rules

- Hospital appointment dates use `YYYY-MM-DD`.
- A patient can have one active appointment; cancelled appointments can be
  booked again.
- Restaurant bills use a 10% discount when the subtotal is at least 1000;
  smaller orders receive no discount.
- Restaurant order quantities must be positive and cannot exceed available
  stock. Updating a quantity to zero removes the item.
- Vehicles have an availability state and cannot be rented twice or returned
  while already available.
