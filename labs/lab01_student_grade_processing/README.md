# Lab 1: Student Grade Processing System

## Aim

Develop a Student Grade Processing System that reads an Excel spreadsheet,
calculates total marks, assigns grades for valid records, and reports invalid
records without assigning a grade.

## Grading policy

| Total marks | Grade |
|---:|:---:|
| 90-100 | A |
| 75-89 | B |
| 60-74 | C |
| 35-59 | D |
| 0-34 | F |

## Files

- `src/processor.py`: mark validation and grade calculation logic
- `src/main.py`: Excel workbook processing and command-line entry point
- `tests/`: pytest tests for grading, validation, and workbook processing
- `data/input/Student_Records_Input.xlsx`: input workbook
- `data/output/Student_Records_Updated.xlsx`: generated workbook with grades
- `docs/test_specification.md`: functional test case specification
- `docs/test_execution_report.md`: manual test execution report
- `docs/test_execution_report.xlsx`: spreadsheet version of the report
- `docs/screenshots/execution_screenshot.png`: program execution screenshot

## Run

From the repository root:

```powershell
.\.venv\Scripts\python .\labs\lab01_student_grade_processing\src\main.py
```

Optional custom paths:

```powershell
.\.venv\Scripts\python .\labs\lab01_student_grade_processing\src\main.py --input <input.xlsx> --output <output.xlsx>
```

## Validation behavior

- Valid rows receive a grade in the existing `Grade` column.
- Invalid rows keep the `Grade` column blank.
- Validation errors are written to an `Error Message` column in the output
  workbook and printed in the execution summary.
