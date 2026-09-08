from task1_wallet.cli import WalletCLI
from task1_wallet.service import WalletService


def test_invalid_menu_choice(capsys):
    cli = WalletCLI(WalletService())
    assert cli.run_once("999") is True
    assert "Invalid menu choice" in capsys.readouterr().out


def test_non_numeric_menu_choice(capsys):
    cli = WalletCLI(WalletService())
    assert cli.run_once("abc") is True
    assert "Invalid menu choice" in capsys.readouterr().out


def test_exit_choice(capsys):
    cli = WalletCLI(WalletService())
    assert cli.run_once("11") is False
    assert "Exiting" in capsys.readouterr().out
