# Google Classroom Submission Bundle

This lab folder is self-contained and can be uploaded as a zip archive.

| Required item | Location |
|---|---|
| Source code | `src/` |
| Unit and integration tests | `tests/` |
| Input/data files | `data/input/` |
| Output files | `data/output/` |
| Execution screenshots | `docs/screenshots/` |
| Test case specification | `docs/test_specification.md` |
| Test execution report | `docs/test_execution_report.md` |
| LaTeX report source | `docs/report.tex` |
| Compiled submission report | `docs/report.pdf` |
| Assignment reference | Repository `labs_pdf/IMG_Batch_Lab_Sheet_4_21_Aug_2026.pdf` |

Before uploading, fill in the student name, roll number, branch, and execution
date in `docs/test_execution_report.md`.

Verified commands:

```powershell
.\.venv\Scripts\python.exe -m pytest .\labs\lab04_real_world_applications\tests -v
.\.venv\Scripts\python.exe -m labs.lab04_real_world_applications.src.main
```
