# Design Notes

## Architectural approach

The implementation uses a small layered design suitable for a laboratory assignment:

1. **Models**: dataclasses/enums represent the application's state.
2. **Service layer**: owns business rules and state transitions.
3. **CLI layer**: reads input, calls services, and displays results.
4. **Tests**: test the service rules directly and test important CLI menu validation separately.

This separation prevents menu code from containing the core transaction/workflow logic and makes the business rules easy to test.

## Task 1 rules

- User ID and Wallet ID are unique.
- Mobile number must be exactly 10 digits.
- Amounts must be finite and strictly greater than zero.
- Blocked wallets cannot participate in money operations.
- Withdrawals and transfers cannot exceed the current balance.
- Source and destination wallets must differ.
- A transfer updates both wallets atomically after validation.
- Every successful operation gets a transaction ID and records the required transaction fields.
- Transfer history is recorded in both involved wallets using the same transaction ID; the global summary counts it once.

## Task 2 rules

- A task belongs to an existing project.
- Priority is one of Low, Medium, High, Critical.
- Status is one of To Do, In Progress, Code Review, Testing, Completed.
- Status can move only to the next workflow state.
- A completed task cannot be completed again.
- A task can be assigned to at most one sprint.
- A task and sprint must belong to the same project.
- Deadline input uses ISO `YYYY-MM-DD` format.
- Project progress is completed project tasks / total project tasks × 100.
- Sprint progress is completed sprint tasks / total sprint tasks × 100.
- For zero tasks, progress is reported as 0.0% to avoid division by zero.

## Why no database?

The supplied lab sheet requires console applications, validation, state management and testing, but does not specify persistent storage or a database. Therefore the implementation uses in-memory dictionaries. This keeps the submission focused on the required software-engineering concepts without introducing unnecessary infrastructure.
