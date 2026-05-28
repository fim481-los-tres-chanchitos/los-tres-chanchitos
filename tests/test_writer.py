import pytest

from los_tres_chanchitos.models import Pig
from los_tres_chanchitos.writer import Writer

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def make_pig(material: str = "paja") -> Pig:
    return Pig(
        material=material,
        personality="perezoso",
        house_description="es fácil de construir.",
        blows_to_fall=1,
    )


@pytest.fixture()
def output() -> list[str]:
    return []


@pytest.fixture()
def writer(output: list[str]) -> Writer:
    return Writer(output.append)


# ---------------------------------------------------------------------------
# Writer.intro
# ---------------------------------------------------------------------------


def test_intro(writer: Writer, output: list[str]) -> None:
    writer.intro(3)
    assert len(output) == 1
    assert "3 chanchitos" in output[0]


# ---------------------------------------------------------------------------
# Writer.wolf_arrives
# ---------------------------------------------------------------------------


def test_wolf_arrives(writer: Writer, output: list[str]) -> None:
    writer.wolf_arrives()
    assert len(output) == 1
    assert "lobo" in output[0]


# ---------------------------------------------------------------------------
# Writer.error
# ---------------------------------------------------------------------------


def test_error(writer: Writer, output: list[str]) -> None:
    writer.error()
    assert len(output) == 1
    assert "ERROR" in output[0]


# ---------------------------------------------------------------------------
# Writer.ending
# ---------------------------------------------------------------------------


def test_ending(writer: Writer, output: list[str]) -> None:
    pig = make_pig(material="ladrillo")
    writer.ending(pig)
    assert len(output) == 3
    combined = "".join(output)
    assert "ladrillo" in combined
    assert "lobo" in combined


# ---------------------------------------------------------------------------
# Writer.building
# ---------------------------------------------------------------------------


def test_building(writer: Writer, output: list[str]) -> None:
    pig = make_pig(material="madera")
    pig_number = 2
    writer.building(pig, pig_number)
    assert len(output) == 4
    combined = "".join(output)
    assert "madera" in combined
    assert str(pig_number) in combined


# ---------------------------------------------------------------------------
# Writer.wolf_knocks
# ---------------------------------------------------------------------------


def test_wolf_knocks_first_time(writer: Writer, output: list[str]) -> None:
    pig = make_pig(material="paja")
    writer.wolf_knocks(pig, blow_number=1)
    assert len(output) == 1
    assert "paja" in output[0]


def test_wolf_knocks_subsequent(writer: Writer, output: list[str]) -> None:
    pig = make_pig(material="paja")
    writer.wolf_knocks(pig, blow_number=2)
    assert len(output) == 1
    assert "otra vez" in output[0]


# ---------------------------------------------------------------------------
# Writer.wolf_threatens_and_blows
# ---------------------------------------------------------------------------


def test_wolf_threatens_and_blows_first(writer: Writer, output: list[str]) -> None:
    writer.wolf_threatens_and_blows(1)
    assert len(output) == 2
    assert "con fuerza" in output[1]


def test_wolf_threatens_and_blows_second(writer: Writer, output: list[str]) -> None:
    writer.wolf_threatens_and_blows(2)
    assert len(output) == 2
    assert "por segunda vez" in output[1]


def test_wolf_threatens_and_blows_tenth(writer: Writer, output: list[str]) -> None:
    writer.wolf_threatens_and_blows(10)
    assert len(output) == 2
    assert "por décima vez" in output[1]


def test_wolf_threatens_and_blows_beyond_tenth(
    writer: Writer, output: list[str]
) -> None:
    writer.wolf_threatens_and_blows(50)
    assert len(output) == 2
    assert "por 50ª vez" in output[1]


# ---------------------------------------------------------------------------
# Writer.house_resists
# ---------------------------------------------------------------------------


def test_house_resists(writer: Writer, output: list[str]) -> None:
    pig = make_pig(material="ladrillo")
    writer.house_resists(pig)
    assert len(output) == 1
    assert "ladrillo" in output[0]
    assert "resistió" in output[0]


# ---------------------------------------------------------------------------
# Writer.house_falls
# ---------------------------------------------------------------------------


def test_house_falls(writer: Writer, output: list[str]) -> None:
    pig = make_pig(material="paja")
    writer.house_falls(pig)
    assert len(output) == 1
    assert "paja" in output[0]
    assert "cayó" in output[0]


# ---------------------------------------------------------------------------
# Writer.pigs_flee
# ---------------------------------------------------------------------------


def test_pigs_flee_one_pig(writer: Writer, output: list[str]) -> None:
    next_pig = make_pig(material="madera")
    writer.pigs_flee(pigs_in_current_house=1, next_pig=next_pig)
    assert len(output) == 1
    assert "madera" in output[0]
    assert "El chanchito corrió" in output[0]


def test_pigs_flee_multiple_pigs(writer: Writer, output: list[str]) -> None:
    next_pig = make_pig(material="ladrillo")
    writer.pigs_flee(pigs_in_current_house=2, next_pig=next_pig)
    assert len(output) == 1
    assert "ladrillo" in output[0]
    assert "Los chanchitos corrieron" in output[0]


# ---------------------------------------------------------------------------
# Writer.house_survives
# ---------------------------------------------------------------------------


def test_house_survives(writer: Writer, output: list[str]) -> None:
    writer.house_survives()
    assert len(output) == 1
    assert "vencido" in output[0]
