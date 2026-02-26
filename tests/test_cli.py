import re

import pytest
from rich import reconfigure

from los_tres_chanchitos.cli import main


def test_main_runs(capsys) -> None:
    exit_code = main([])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "Hola, mundo!" in out


def test_main_runs_with_custom_name(capsys) -> None:
    exit_code = main(["FIM481"])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "Hola, FIM481!" in out


def test_main_version_flag_prints_version(capsys) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])

    assert excinfo.value.code == 0
    out = capsys.readouterr().out
    assert re.fullmatch(r"los-tres-chanchitos \d+\.\d+\.\d+", out.strip())


def test_main_renders_green_ansi(capsys) -> None:
    reconfigure(force_terminal=True, color_system="standard")
    exit_code = main(["FIM481"])

    assert exit_code == 0
    out = capsys.readouterr().out
    assert re.search(r"Hola, \x1b\[[0-9;]*mFIM481\x1b\[[0-9;]*m!", out)
