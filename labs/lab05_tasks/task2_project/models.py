from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class TaskStatus(str, Enum):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    CODE_REVIEW = "Code Review"
    TESTING = "Testing"
    COMPLETED = "Completed"


WORKFLOW = [
    TaskStatus.TO_DO,
    TaskStatus.IN_PROGRESS,
    TaskStatus.CODE_REVIEW,
    TaskStatus.TESTING,
    TaskStatus.COMPLETED,
]


@dataclass(frozen=True)
class Project:
    name: str


@dataclass
class Task:
    task_id: str
    title: str
    project_name: str
    assigned_developer: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    sprint_id: Optional[str] = None
    deadline: Optional[date] = None
    status: TaskStatus = TaskStatus.TO_DO


@dataclass(frozen=True)
class Sprint:
    sprint_id: str
    project_name: str
