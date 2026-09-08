# Lab 4 Test Execution Report

## Student details

| Field | Value |
|---|---|
| Name | Nishant Harkut |
| Roll number | 2023IMG-040 |
| Branch | IMG |
| Batch | IMG |
| Course | Software Engineering Laboratory |
| Experiment | 4 |
| Execution date | 21 August 2026 |

## Automated execution

Run from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pytest .\labs\lab04_real_world_applications\tests -v
```

| Test area | Result |
|---|---|
| Hospital domain tests | 6 passed |
| Restaurant domain tests | 6 passed |
| Vehicle domain tests | 5 passed |
| Console menu integration test | 1 passed |
| Lab 4 result | 18 passed |
| Full semester suite | 66 passed |

Verified command output for the complete repository suite:

```text
66 passed in 1.08s
```

## Required test-case evidence

| TC ID | Input / scenario | Actual result | PASS/FAIL |
|---|---|---|---|
| TC-01 | Valid patient record | Patient added successfully | PASS |
| TC-02 | Duplicate patient ID | Duplicate patient ID error | PASS |
| TC-03 | Invalid appointment date | Date validation error | PASS |
| TC-04 | Appointment already booked | Booking rejected | PASS |
| TC-05 | Valid food item | Food item added successfully | PASS |
| TC-06 | Duplicate food ID | Duplicate food ID error | PASS |
| TC-07 | Quantity greater than stock | Stock validation error | PASS |
| TC-08 | Discount boundary bill | Correct subtotal, discount, and total | PASS |
| TC-09 | Rent available vehicle | Vehicle marked rented | PASS |
| TC-10 | Rent already rented vehicle | Rental state error | PASS |
| TC-11 | Return available vehicle | Return state error | PASS |
| TC-12 | Invalid menu/numerical input | Input rejected with error message | PASS |

## Manual demonstration checklist

- [ ] Add and display a hospital patient.
- [ ] Search for a patient and demonstrate a missing ID error.
- [ ] Book, update, display by doctor, cancel, and report an appointment.
- [ ] Add and search restaurant food items.
- [ ] Add, remove, and update order quantities.
- [ ] Calculate subtotal, apply the discount rule, and generate the final bill.
- [ ] Add, search, rent, return, and filter vehicles by availability.
- [ ] Enter an invalid menu choice and invalid numerical input.
