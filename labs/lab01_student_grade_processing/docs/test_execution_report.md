# Lab 1 Test Execution Report

Command executed:

```powershell
.\.venv\Scripts\python .\labs\lab01_student_grade_processing\src\main.py
```

| Test Case ID | Scenario | Expected Result | Actual Result | PASS/FAIL | Error Message (if applicable) |
|---|---|---|---|---|---|
| TC-01 | Invalid total/range | No grade is assigned for invalid marks. | Grade column remained blank. | PASS | End examination marks out of range |
| TC-02 | Valid student record | Grade `C` is written for total marks of 60. | Grade `C` was written. | PASS | Not applicable |
| TC-03 | Missing input | No grade is assigned when a marks field is blank. | Grade column remained blank. | PASS | Missing input |
| TC-04 | Invalid data type | No grade is assigned when a marks field is non-numeric. | Grade column remained blank. | PASS | Invalid data type |

All four functional test cases match the expected behavior from the lab sheet.
