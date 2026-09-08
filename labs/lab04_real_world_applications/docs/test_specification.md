# Lab 4 Test Specification

The test design covers the three applications independently so a failure in
one business area does not hide a failure in another.

| ID | Application | Scenario | Expected result |
|---|---|---|---|
| TC-01 | Hospital | Add a valid patient | Patient is stored successfully |
| TC-02 | Hospital | Add a duplicate patient ID | Duplicate ID error |
| TC-03 | Hospital | Book with invalid date | Date validation error |
| TC-04 | Hospital | Book an already booked patient | Appointment already booked error |
| TC-05 | Restaurant | Add a valid food item | Food item is stored successfully |
| TC-06 | Restaurant | Add a duplicate food ID | Duplicate ID error |
| TC-07 | Restaurant | Add quantity greater than stock | Stock validation error |
| TC-08 | Restaurant | Generate a bill at the discount boundary | Correct subtotal, discount, and total |
| TC-09 | Vehicle | Rent an available vehicle | Vehicle becomes rented |
| TC-10 | Vehicle | Rent an already rented vehicle | Rental state error |
| TC-11 | Vehicle | Return an available vehicle | Return state error |
| TC-12 | All | Invalid numerical input or menu choice | Input is rejected with an error message |

The assignment requires at least 10 test cases. Twelve are specified here to
cover all three systems and the common input-handling requirement.
