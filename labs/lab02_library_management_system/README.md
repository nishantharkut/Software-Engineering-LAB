# Lab 2: Library Management System

## Aim

Develop a Library Management System that reads an Excel spreadsheet, validates
book records, determines the current status, and reports invalid records.

## Validation Rule

```
Total Copies = Available Copies + Issued Copies
```

## Status Policy

| Condition | Status |
|:----------|:-------|
| Available Copies > 0 | Available |
| Available Copies = 0 | Issued Out |

Invalid records leave the Status column blank.

## Files

- `src/processor.py`: book record validation and status determination logic
- `src/main.py`: Excel workbook processing and command-line entry point
- `tests/`: pytest tests for validation, status, and workbook processing
- `data/input/Library_Records_Input.xlsx`: input workbook
- `data/output/Library_Records_Updated.xlsx`: generated workbook with status
- `docs/test_specification.md`: functional test case specification

## Run

From the repository root:

```powershell
.\.venv\Scripts\python .\labs\lab02_library_management_system\src\main.py
```

Optional custom paths:

```powershell
.\.venv\Scripts\python .\labs\lab02_library_management_system\src\main.py --input <input.xlsx> --output <output.xlsx>
```

## Run Tests

From the repository root:

```powershell
.\.venv\Scripts\python -m pytest .\labs\lab02_library_management_system\tests -v
```

From the lab directory:

```powershell
.\.venv\Scripts\python -m pytest tests -v
```

## Validation Behavior

- Valid rows receive a status ("Available" or "Issued Out") in the `Status` column.
- Invalid rows keep the `Status` column blank.
- Validation errors are displayed in the execution summary.