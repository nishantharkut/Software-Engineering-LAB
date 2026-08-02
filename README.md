# Software Engineering Laboratory

Semester lab repository for Software Engineering Laboratory coursework.

The repository is organized so each experiment is isolated, reproducible, and easy
to review. Lab 1 is complete; later labs can be added as sibling folders under
`labs/` without changing the existing submission.

`Software_Engineering_Labs.ipynb` is the cumulative notebook for the semester. It
records the runnable execution and observed results for each lab while the full
source files and deliverables stay inside the matching lab folder.

## Repository structure

```text
.
|-- labs/
|   `-- lab01_student_grade_processing/
|       |-- data/
|       |   |-- input/
|       |   `-- output/
|       |-- docs/
|       |-- src/
|       |-- tests/
|       `-- README.md
|-- Lab sheet SE-1.pdf
|-- Software_Engineering_Labs.ipynb
|-- pyproject.toml
`-- requirements.txt
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Run Lab 1

From the repository root:

```powershell
.\.venv\Scripts\python .\labs\lab01_student_grade_processing\src\main.py
```

The program reads the input workbook from `data/input/`, writes the updated
workbook to `data/output/`, and prints a validation summary.

## Run tests

```powershell
.\.venv\Scripts\python -m pytest
```

Each lab keeps its own tests under `labs/<lab_name>/tests/`. Lab 1 tests cover
the grading policy, validation errors, and the Excel processing pipeline required
by the lab sheet.

## Adding later labs

Add each new experiment as `labs/labNN_short_name/` with the same basic shape:

- `src/` for source code
- `data/input/` and `data/output/` for lab artifacts
- `docs/` for reports, screenshots, and notes
- `tests/` for lab-specific pytest tests
- `README.md` for lab-specific instructions
