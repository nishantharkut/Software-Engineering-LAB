# Lab 1 Test Specification

The following functional test cases validate the Student Grade Processing System
against the Lab Sheet 1 requirements.

| Test Case ID | Scenario | Test Data | Expected Result |
|---|---|---|---|
| TC-01 | Invalid total/range | Project=20, Minor=20, Laboratory=20, End Examination=41 | No grade is assigned. The program reports an appropriate validation error. |
| TC-02 | Valid student record | Total marks=60 | Grade `C` is written to the `Grade` column. |
| TC-03 | Missing input | One marks field is blank | No grade is assigned. The program reports missing input. |
| TC-04 | Invalid data type | One marks field contains `AB` | No grade is assigned. The program reports invalid data type. |

Automated pytest coverage is provided for grading boundaries, validation errors,
and the Excel processing pipeline.
