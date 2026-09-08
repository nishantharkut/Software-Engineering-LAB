from .exceptions import ProjectError
from .service import ProjectService


class ProjectCLI:
    def __init__(self, service: ProjectService | None = None):
        self.service = service or ProjectService()

    def display_menu(self):
        print("\n=== Software Project Task Management & Sprint Tracking ===")
        options = [
            "Create software project", "Add project task", "Display all tasks", "Search task by Task ID",
            "Assign developer", "Set/update priority", "Set/update deadline", "Create sprint",
            "Assign task to sprint", "Update task status", "Display pending tasks", "Display completed tasks",
            "Display tasks for developer", "Calculate project progress", "Generate sprint progress report", "Exit",
        ]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    def run_once(self, choice: str) -> bool:
        try:
            choice = int(choice)
        except (TypeError, ValueError):
            print("Invalid menu choice. Please enter a number.")
            return True
        actions = {
            1: self._create_project, 2: self._create_task, 3: self._display_tasks, 4: self._search,
            5: self._assign_developer, 6: self._priority, 7: self._deadline, 8: self._create_sprint,
            9: self._assign_sprint, 10: self._status, 11: self._pending, 12: self._completed,
            13: self._developer_tasks, 14: self._project_progress, 15: self._sprint_report,
        }
        if choice == 16:
            print("Exiting...")
            return False
        action = actions.get(choice)
        if not action:
            print("Invalid menu choice. Please choose 1-16.")
            return True
        try:
            action()
        except ProjectError as exc:
            print(f"Error: {exc}")
        return True

    def _create_project(self):
        self.service.create_project(input("Project name: "))
        print("Project created successfully.")

    def _create_task(self):
        self.service.create_task(input("Task ID: "), input("Task title: "), input("Project name: "), input("Priority [Medium]: ") or "Medium", input("Deadline [YYYY-MM-DD, optional]: ") or None)
        print("Task created successfully.")

    def _display_tasks(self):
        for task in self.service.list_tasks():
            print(task)

    def _search(self): print(self.service.search_task(input("Task ID: ")))
    def _assign_developer(self): self.service.assign_developer(input("Task ID: "), input("Developer: ")); print("Developer assigned successfully.")
    def _priority(self): self.service.set_priority(input("Task ID: "), input("Priority: ")); print("Priority updated successfully.")
    def _deadline(self): self.service.set_deadline(input("Task ID: "), input("Deadline [YYYY-MM-DD]: ")); print("Deadline updated successfully.")
    def _create_sprint(self): self.service.create_sprint(input("Sprint ID: "), input("Project name: ")); print("Sprint created successfully.")
    def _assign_sprint(self): self.service.assign_task_to_sprint(input("Task ID: "), input("Sprint ID: ")); print("Task assigned to sprint successfully.")
    def _status(self): self.service.update_status(input("Task ID: "), input("New status: ")); print("Task status updated successfully.")
    def _pending(self):
        for task in self.service.pending_tasks(): print(task)
    def _completed(self):
        for task in self.service.completed_tasks(): print(task)
    def _developer_tasks(self):
        for task in self.service.tasks_for_developer(input("Developer: ")): print(task)
    def _project_progress(self): print(f"Project progress: {self.service.project_progress(input('Project name: ')):.2f}%")
    def _sprint_report(self):
        report = self.service.sprint_report(input("Sprint ID: "))
        for key, value in report.items(): print(f"{key.replace('_', ' ').title()}: {value}")

    def run(self):
        while True:
            self.display_menu()
            if not self.run_once(input("Enter choice: ")):
                break


def main():
    ProjectCLI().run()


if __name__ == "__main__":
    main()
