# Software Engineering Laboratory – Experiment 5

Implementation of both tasks from the IIITM Gwalior Software Engineering Laboratory Lab Sheet 5 (25 August 2026), using Python 3 and pytest.

## Structure

```text
SE_Lab5_Solution/
├── task1_wallet/
│   ├── __init__.py
│   ├── models.py
│   ├── exceptions.py
│   ├── service.py
│   └── cli.py
├── task2_project/
│   ├── __init__.py
│   ├── models.py
│   ├── exceptions.py
│   ├── service.py
│   └── cli.py
├── tests/
│   ├── test_wallet.py
│   ├── test_wallet_cli.py
│   ├── test_project.py
│   └── test_project_cli.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Design

Both applications use:

- `models.py` – domain entities and enums.
- `exceptions.py` – application-specific validation/business-rule errors.
- `service.py` – business logic, validation, state changes and reports.
- `cli.py` – menu-driven console interface only; it delegates business rules to the service layer.
- `tests/` – automated pytest tests, including valid, invalid and boundary scenarios.

Data is kept in memory because the lab sheet does not require a database or file persistence.

## Run

```bash
python -m pip install -r requirements.txt
pytest
```

Run the applications:

```bash
python -m task1_wallet.cli
python -m task2_project.cli
```

## Requirement coverage

### Task 1 – Digital Wallet

Implements wallet creation, listing, search, deposit, withdrawal, transfer, balance, transaction history, block/unblock and transaction summary. It validates duplicate IDs, missing wallets, empty names, mobile numbers, non-positive amounts, insufficient balance, invalid transfers, blocked wallets, invalid numerical input and invalid menu choices.

Successful transactions record transaction ID, type, source wallet, destination wallet, amount and updated balance.

### Task 2 – Project / Task / Sprint Tracking

Implements project creation, task creation/search/listing, developer assignment, priority/deadline updates, sprint creation, task-to-sprint assignment, status updates, pending/completed/developer views, project progress and sprint reports.

The enforced workflow is:

`To Do → In Progress → Code Review → Testing → Completed`

Only the next state in this workflow is allowed.

## Test cases

The automated suite contains more than the required 10 scenarios per task and explicitly covers the lab sheet's requested categories. `pytest` output is the actual execution result.
