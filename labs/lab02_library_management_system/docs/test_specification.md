# Lab 2 Test Specification

The following functional test cases validate the Library Management System
against the Lab Sheet 2 requirements.

| Test Case ID | Scenario | Test Data | Expected Result |
|---|---|---|---|
| TC-01 | Invalid Book Record | Total=10, Available=7, Issued=5 (7+5≠10) | Status remains blank. Error message displayed. |
| TC-02 | Book Completely Issued | Total=5, Available=0, Issued=5 | Status is "Issued Out". |
| TC-03 | Missing Input | One field (Total/Available/Issued) is blank | Status remains blank. Error message: "Missing input". |
| TC-04 | Invalid Data Type | Available="Five" instead of numeric | Status remains blank. Error message: "Invalid data type". |
| TC-05 | Negative Inventory | Available=-2, Issued=12, Total=10 | Status remains blank. Error message: "Negative inventory value". |

Automated pytest coverage is provided for:
- Parse and validation functions (missing input, invalid types, negative values)
- Constraint validation (Total ≠ Available + Issued)
- Status determination (Available vs Issued Out)
- Excel processing pipeline