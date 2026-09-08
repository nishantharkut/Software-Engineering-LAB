# Test Cases and Execution Results

The lab requires at least 10 test cases for each task, including valid and invalid scenarios. This implementation has 54 automated pytest checks in total and covers substantially more than the minimum.

## Task 1 – Digital Wallet

| TC ID | Input / Scenario | Expected Result | Actual Result | PASS/FAIL |
|---|---|---|---|---|
| W-TC-01 | Create valid wallet | Wallet added successfully | Wallet created with zero balance | PASS |
| W-TC-02 | Duplicate User ID | Appropriate error | `DuplicateError` raised | PASS |
| W-TC-03 | Duplicate Wallet ID | Appropriate error | `DuplicateError` raised | PASS |
| W-TC-04 | Search non-existing Wallet ID | Appropriate error | `NotFoundError` raised | PASS |
| W-TC-05 | Empty user name | Input rejected | `ValidationError` raised | PASS |
| W-TC-06 | Invalid mobile number | Input rejected | `ValidationError` raised | PASS |
| W-TC-07 | Non-numeric deposit | Input rejected | `ValidationError` raised | PASS |
| W-TC-08 | Zero/negative deposit | Input rejected | `ValidationError` raised | PASS |
| W-TC-09 | Valid deposit | Balance increases and history records transaction | Balance/history updated correctly | PASS |
| W-TC-10 | Insufficient withdrawal | Appropriate error; balance unchanged | `InsufficientBalanceError` raised | PASS |
| W-TC-11 | Valid withdrawal | Balance decreases correctly | Correct balance/history | PASS |
| W-TC-12 | Transfer to missing wallet | Appropriate error | `NotFoundError` raised | PASS |
| W-TC-13 | Transfer to same wallet | Appropriate error | `ValidationError` raised | PASS |
| W-TC-14 | Transfer involving blocked wallet | Appropriate error | `BlockedWalletError` raised | PASS |
| W-TC-15 | Valid transfer | Both balances and histories update | Correct source/destination balances | PASS |
| W-TC-16 | Transfer/withdraw beyond balance | Wallet must not become negative | Operation rejected; balance unchanged | PASS |
| W-TC-17 | Block then unblock wallet | Status changes correctly | Blocked → Active | PASS |
| W-TC-18 | Generate transaction summary | Correct totals | Unique transaction totals calculated | PASS |

## Task 2 – Software Project / Sprint Tracking

| TC ID | Input / Scenario | Expected Result | Actual Result | PASS/FAIL |
|---|---|---|---|---|
| P-TC-01 | Create valid project | Project created | Project stored | PASS |
| P-TC-02 | Empty project name | Input rejected | `ValidationError` raised | PASS |
| P-TC-03 | Duplicate project | Appropriate error | `DuplicateError` raised | PASS |
| P-TC-04 | Create valid task | Task created with default To Do/Medium | Correct defaults | PASS |
| P-TC-05 | Duplicate Task ID | Appropriate error | `DuplicateError` raised | PASS |
| P-TC-06 | Search missing Task ID | Appropriate error | `NotFoundError` raised | PASS |
| P-TC-07 | Empty task title | Input rejected | `ValidationError` raised | PASS |
| P-TC-08 | Invalid priority | Input rejected | `ValidationError` raised | PASS |
| P-TC-09 | Invalid task status | Input rejected | `ValidationError` raised | PASS |
| P-TC-10 | Empty developer assignment | Input rejected | `ValidationError` raised | PASS |
| P-TC-11 | Valid developer assignment/filter | Developer tasks returned | Correct task returned | PASS |
| P-TC-12 | Invalid deadline format | Input rejected | `ValidationError` raised | PASS |
| P-TC-13 | Valid deadline | Deadline updated | Correct `date` stored | PASS |
| P-TC-14 | Assign task to missing sprint | Appropriate error | `NotFoundError` raised | PASS |
| P-TC-15 | Assign task already in sprint | Appropriate error | `ValidationError` raised | PASS |
| P-TC-16 | Skip workflow state | Appropriate error | `StateTransitionError` raised | PASS |
| P-TC-17 | Complete full workflow | To Do → In Progress → Code Review → Testing → Completed | Completed successfully | PASS |
| P-TC-18 | Complete already completed task | Appropriate error | `StateTransitionError` raised | PASS |
| P-TC-19 | Pending/completed filtering | Correct task groups | Correct lists returned | PASS |
| P-TC-20 | Project progress with no tasks | 0% | 0.0% | PASS |
| P-TC-21 | Project progress with 1/2 completed | 50% | 50.0% | PASS |
| P-TC-22 | Sprint progress report | Correct totals and percentage | Correct report | PASS |
| P-TC-23 | 100% sprint | 100% when all sprint tasks completed | 100.0% | PASS |
| P-TC-24 | Task/sprint different projects | Assignment rejected | `ValidationError` raised | PASS |

## CLI validation tests

Both CLIs also test non-numeric menu input, out-of-range menu choices, and exit behavior.

## Pytest execution

Command:

```bash
python -m pytest -q
```

Observed result:

```text
54 passed
```
