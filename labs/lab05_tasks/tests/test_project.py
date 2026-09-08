from datetime import date
import pytest

from task2_project.exceptions import DuplicateError, NotFoundError, StateTransitionError, ValidationError
from task2_project.models import Priority, TaskStatus
from task2_project.service import ProjectService


def project_service():
    s = ProjectService()
    s.create_project("Alpha")
    s.create_task("T1", "Build API", "Alpha")
    s.create_task("T2", "Build UI", "Alpha", priority="High", deadline="2026-12-31")
    s.create_sprint("S1", "Alpha")
    return s


def test_valid_project_creation():
    s = ProjectService(); p = s.create_project("Alpha")
    assert p.name == "Alpha"


def test_empty_project_name_rejected():
    with pytest.raises(ValidationError): ProjectService().create_project("   ")


def test_duplicate_project_rejected():
    s = ProjectService(); s.create_project("Alpha")
    with pytest.raises(DuplicateError): s.create_project("Alpha")


def test_valid_task_creation():
    s = ProjectService(); s.create_project("Alpha")
    t = s.create_task("T1", "Build API", "Alpha")
    assert t.status == TaskStatus.TO_DO and t.priority == Priority.MEDIUM


def test_duplicate_task_id_rejected():
    s = project_service()
    with pytest.raises(DuplicateError): s.create_task("T1", "Other", "Alpha")


def test_task_id_not_found():
    with pytest.raises(NotFoundError): project_service().search_task("T404")


def test_empty_task_title_rejected():
    s = ProjectService(); s.create_project("Alpha")
    with pytest.raises(ValidationError): s.create_task("T1", "", "Alpha")


def test_empty_project_name_for_task_rejected():
    with pytest.raises(ValidationError): ProjectService().create_task("T1", "Task", "")


def test_non_existing_project_for_task_rejected():
    with pytest.raises(NotFoundError): ProjectService().create_task("T1", "Task", "Missing")


def test_invalid_priority_rejected():
    s = project_service()
    with pytest.raises(ValidationError): s.set_priority("T1", "Urgent")


def test_invalid_status_rejected():
    with pytest.raises(ValidationError): project_service().update_status("T1", "Done")


def test_invalid_developer_assignment_rejected():
    with pytest.raises(ValidationError): project_service().assign_developer("T1", "   ")


def test_valid_developer_assignment_and_filter():
    s = project_service(); s.assign_developer("T1", "Dev A")
    assert [t.task_id for t in s.tasks_for_developer("Dev A")] == ["T1"]


def test_invalid_deadline_rejected():
    with pytest.raises(ValidationError): project_service().set_deadline("T1", "31-12-2026")


def test_valid_deadline():
    s = project_service(); s.set_deadline("T1", "2026-11-30")
    assert s.search_task("T1").deadline == date(2026, 11, 30)


def test_assign_task_to_non_existing_sprint_rejected():
    with pytest.raises(NotFoundError): project_service().assign_task_to_sprint("T1", "S404")


def test_assign_task_already_in_sprint_rejected():
    s = project_service(); s.assign_task_to_sprint("T1", "S1")
    s.create_sprint("S2", "Alpha")
    with pytest.raises(ValidationError): s.assign_task_to_sprint("T1", "S2")


def test_invalid_status_transition_rejected():
    s = project_service()
    with pytest.raises(StateTransitionError): s.update_status("T1", "Testing")
    assert s.search_task("T1").status == TaskStatus.TO_DO


def test_complete_workflow():
    s = project_service()
    for status in ["In Progress", "Code Review", "Testing", "Completed"]:
        s.update_status("T1", status)
    assert s.search_task("T1").status == TaskStatus.COMPLETED


def test_completing_already_completed_rejected():
    s = project_service()
    for status in ["In Progress", "Code Review", "Testing", "Completed"]: s.update_status("T1", status)
    with pytest.raises(StateTransitionError): s.update_status("T1", "Completed")


def test_pending_and_completed_lists():
    s = project_service()
    for status in ["In Progress", "Code Review", "Testing", "Completed"]: s.update_status("T1", status)
    assert [t.task_id for t in s.completed_tasks()] == ["T1"]
    assert [t.task_id for t in s.pending_tasks()] == ["T2"]


def test_project_progress_boundary_zero_tasks():
    s = ProjectService(); s.create_project("Empty")
    assert s.project_progress("Empty") == 0.0


def test_project_progress():
    s = project_service()
    for status in ["In Progress", "Code Review", "Testing", "Completed"]: s.update_status("T1", status)
    assert s.project_progress("Alpha") == 50.0


def test_sprint_progress_report():
    s = project_service(); s.assign_task_to_sprint("T1", "S1"); s.assign_task_to_sprint("T2", "S1")
    s.update_status("T1", "In Progress")
    report = s.sprint_report("S1")
    assert report == {"sprint_id": "S1", "total_tasks": 2, "completed_tasks": 0, "pending_tasks": 2, "tasks_in_progress": 1, "progress_percentage": 0.0}


def test_sprint_report_after_completion():
    s = project_service(); s.assign_task_to_sprint("T1", "S1")
    for status in ["In Progress", "Code Review", "Testing", "Completed"]: s.update_status("T1", status)
    assert s.sprint_report("S1")["progress_percentage"] == 100.0


def test_task_and_sprint_must_belong_to_same_project():
    s = ProjectService(); s.create_project("Alpha"); s.create_project("Beta")
    s.create_task("T1", "Task", "Alpha"); s.create_sprint("S2", "Beta")
    with pytest.raises(ValidationError): s.assign_task_to_sprint("T1", "S2")
