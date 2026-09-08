from labs.lab04_real_world_applications.src.main import main


def test_top_level_menu_handles_invalid_choice_and_exits(monkeypatch, capsys):
    answers = iter(["9", "4"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    main()

    output = capsys.readouterr().out
    assert "Invalid menu choice" in output
    assert "Goodbye" in output
