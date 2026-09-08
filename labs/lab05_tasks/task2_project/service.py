from datetime import date, datetime
from typing import Optional

from .exceptions import DuplicateError, NotFoundError, StateTransitionError, ValidationError
from .models import Priority, Project, Sprint, Task, TaskStatus, WORKFLOW


class ProjectService:
    """Business logic for projects, tasks and sprints."""

    def __init__(self) -> None:
        self.projects: dict[str, Project] = {}
        self.tasks: dict[str, Task] = {}
        self.sprints: dict[str, Sprint] = {}

    @staticmethod
    def _required_text(value: str, field: str) -> str:
        value = str(value).strip()
        if not value:
            raise ValidationError(f"{field} cannot be empty.")
        return value

    def create_project(self, project_name: str) -> Project:
        project_name = self._required_text(project_name, "Project name")
        if project_name in self.projects:
            raise DuplicateError(f"Project '{project_name}' already exists.")
        project = Project(project_name)
        self.projects[project_name] = project
        return project

    def _get_project(self, project_name: str) -> Project:
        if project_name not in self.projects:
            raise NotFoundError(f"Project '{project_name}' not found.")
        return self.projects[project_name]

    def create_task(self, task_id: str, title: str, project_name: str, priority: str = "Medium", deadline: str | date | None = None) -> Task:
        task_id = self._required_text(task_id, "Task ID")
        title = self._required_text(title, "Task title")
        project_name = self._required_text(project_name, "Project name")
        self._get_project(project_name)
        if task_id in self.tasks:
            raise DuplicateError(f"Task ID '{task_id}' already exists.")
        task = Task(task_id, title, project_name, priority=self._parse_priority(priority), deadline=self._parse_deadline(deadline))
        self.tasks[task_id] = task
        return task

    def _get_task(self, task_id: str) -> Task:
        task_id = str(task_id).strip()
        if task_id not in self.tasks:
            raise NotFoundError(f"Task '{task_id}' not found.")
        return self.tasks[task_id]

    def list_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    def search_task(self, task_id: str) -> Task:
        return self._get_task(task_id)

    @staticmethod
    def _parse_priority(priority: str | Priority) -> Priority:
        try:
            return priority if isinstance(priority, Priority) else Priority(str(priority).strip().title())
        except ValueError:
            raise ValidationError("Invalid priority. Use Low, Medium, High or Critical.")

    @staticmethod
    def _parse_status(status: str | TaskStatus) -> TaskStatus:
        try:
            if isinstance(status, TaskStatus):
                return status
            normalized = str(status).strip().lower()
            for item in TaskStatus:
                if normalized == item.value.lower():
                    return item
            raise ValueError
        except ValueError:
            raise ValidationError("Invalid task status.")

    @staticmethod
    def _parse_deadline(deadline: str | date | None) -> Optional[date]:
        if deadline is None or (isinstance(deadline, str) and not deadline.strip()):
            return None
        if isinstance(deadline, date):
            return deadline
        try:
            return datetime.strptime(str(deadline).strip(), "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError("Invalid deadline. Use YYYY-MM-DD.")

    def assign_developer(self, task_id: str, developer: str) -> Task:
        task = self._get_task(task_id)
        developer = self._required_text(developer, "Developer assignment")
        task.assigned_developer = developer
        return task

    def set_priority(self, task_id: str, priority: str | Priority) -> Task:
        task = self._get_task(task_id)
        task.priority = self._parse_priority(priority)
        return task

    def set_deadline(self, task_id: str, deadline: str | date) -> Task:
        task = self._get_task(task_id)
        task.deadline = self._parse_deadline(deadline)
        return task

    def create_sprint(self, sprint_id: str, project_name: str) -> Sprint:
        sprint_id = self._required_text(sprint_id, "Sprint ID")
        project_name = self._required_text(project_name, "Project name")
        self._get_project(project_name)
        if sprint_id in self.sprints:
            raise DuplicateError(f"Sprint ID '{sprint_id}' already exists.")
        sprint = Sprint(sprint_id, project_name)
        self.sprints[sprint_id] = sprint
        return sprint

    def assign_task_to_sprint(self, task_id: str, sprint_id: str) -> Task:
        task = self._get_task(task_id)
        sprint_id = self._required_text(sprint_id, "Sprint ID")
        if sprint_id not in self.sprints:
            raise NotFoundError(f"Sprint '{sprint_id}' not found.")
        sprint = self.sprints[sprint_id]
        if task.sprint_id is not None:
            raise ValidationError(f"Task '{task_id}' is already assigned to sprint '{task.sprint_id}'.")
        if task.project_name != sprint.project_name:
            raise ValidationError("Task and sprint must belong to the same project.")
        task.sprint_id = sprint_id
        return task

    def update_status(self, task_id: str, new_status: str | TaskStatus) -> Task:
        task = self._get_task(task_id)
        new_status = self._parse_status(new_status)
        current_index = WORKFLOW.index(task.status)
        new_index = WORKFLOW.index(new_status)
        if new_index != current_index + 1:
            if task.status == TaskStatus.COMPLETED and new_status == TaskStatus.COMPLETED:
                raise StateTransitionError("Task is already completed.")
            raise StateTransitionError(f"Invalid status transition: {task.status.value} -> {new_status.value}.")
        task.status = new_status
        return task

    def pending_tasks(self) -> list[Task]:
        return [t for t in self.tasks.values() if t.status != TaskStatus.COMPLETED]

    def completed_tasks(self) -> list[Task]:
        return [t for t in self.tasks.values() if t.status == TaskStatus.COMPLETED]

    def tasks_for_developer(self, developer: str) -> list[Task]:
        developer = self._required_text(developer, "Developer")
        return [t for t in self.tasks.values() if t.assigned_developer == developer]

    def project_progress(self, project_name: str) -> float:
        self._get_project(project_name)
        project_tasks = [t for t in self.tasks.values() if t.project_name == project_name]
        if not project_tasks:
            return 0.0
        return round(len([t for t in project_tasks if t.status == TaskStatus.COMPLETED]) / len(project_tasks) * 100, 2)

    def sprint_report(self, sprint_id: str) -> dict:
        sprint_id = self._required_text(sprint_id, "Sprint ID")
        if sprint_id not in self.sprints:
            raise NotFoundError(f"Sprint '{sprint_id}' not found.")
        sprint_tasks = [t for t in self.tasks.values() if t.sprint_id == sprint_id]
        total = len(sprint_tasks)
        completed = sum(t.status == TaskStatus.COMPLETED for t in sprint_tasks)
        in_progress = sum(t.status == TaskStatus.IN_PROGRESS for t in sprint_tasks)
        pending = total - completed
        progress = round(completed / total * 100, 2) if total else 0.0
        return {
            "sprint_id": sprint_id,
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending,
            "tasks_in_progress": in_progress,
            "progress_percentage": progress,
        }
