from task2_project.cli import ProjectCLI
from task2_project.service import ProjectService


def test_invalid_menu_choice(capsys):
    cli = ProjectCLI(ProjectService())
    assert cli.run_once("999") is True
    assert "Invalid menu choice" in capsys.readouterr().out


def test_non_numeric_menu_choice(capsys):
    cli = ProjectCLI(ProjectService())
    assert cli.run_once("abc") is True
    assert "Invalid menu choice" in capsys.readouterr().out


def test_exit_choice(capsys):
    cli = ProjectCLI(ProjectService())
    assert cli.run_once("16") is False
    assert "Exiting" in capsys.readouterr().out
