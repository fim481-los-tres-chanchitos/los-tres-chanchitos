import re

import pytest

from los_tres_chanchitos.cli import main


def test_main_runs(capsys) -> None:
    exit_code = main([])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "Había una vez 3 chanchitos" in out


def test_main_prints_wolf_attack(capsys) -> None:
    exit_code = main([])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "¡Soplaré y soplaré, y tu casa derribaré!" in out


def test_main_prints_ending(capsys) -> None:
    exit_code = main([])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "salvo" in out


def test_main_version_flag_prints_version(capsys) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])

    assert excinfo.value.code == 0
    out = capsys.readouterr().out
    assert re.fullmatch(r"los-tres-chanchitos \d+\.\d+\.\d+", out.strip())
