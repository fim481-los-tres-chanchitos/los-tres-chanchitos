from los_tres_chanchitos.models import Pig, Scenario, Wolf
from los_tres_chanchitos.narrator import Narrator
from los_tres_chanchitos.writer import Writer


def test_pigs_are_numbered_starting_from_1() -> None:
    wolf = Wolf(blows_limit=3)
    pig = Pig(
        material="ladrillos",
        personality="el más trabajador",
        house_description="tardó mucho en construirse pero quedó muy sólida.",
        blows_to_fall=None,
    )
    scenario = Scenario(pigs=[pig], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "El chanchito 1," in out
    assert "El chanchito 0," not in out


def test_single_pig_indestructible_house() -> None:
    blows_limit = 3
    wolf = Wolf(blows_limit=blows_limit)
    pig = Pig(
        material="ladrillos",
        personality="el más trabajador",
        house_description="tardó mucho en construirse pero quedó muy sólida.",
        blows_to_fall=None,
    )
    scenario = Scenario(pigs=[pig], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "Había una vez 1 chanchitos" in out
    assert out.count("¡Soplaré y soplaré, y tu casa derribaré!") == blows_limit
    assert out.count("La casa de ladrillos resistió.") == blows_limit
    assert "Al ver que no podía derribarla, el lobo se dio por vencido." in out
    assert (
        "Los chanchitos se quedaron juntos en la casa de ladrillos, contentos y a salvo."
        in out
    )
    assert "corrieron hacia la casa de" not in out


def test_single_pig_fragile_house() -> None:
    blows_to_fall = 2
    blows_limit = 3
    wolf = Wolf(blows_limit=blows_limit)
    pig = Pig(
        material="madera",
        personality="dispuesto a trabajar un poco más",
        house_description="se levanta con más trabajo, aunque puede romperse.",
        blows_to_fall=blows_to_fall,
    )
    scenario = Scenario(pigs=[pig], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "Había una vez 1 chanchitos" in out
    assert out.count("¡Soplaré y soplaré, y tu casa derribaré!") == blows_to_fall
    assert out.count("La casa de madera resistió.") == blows_to_fall - 1
    assert "La casa de madera cayó." in out
    assert "Al ver que no podía derribarla, el lobo se dio por vencido." not in out
    assert "Entonces el lobo trató de entrar por la chimenea" not in out
    assert "contentos y a salvo." not in out
    assert "*** ERROR: escenario inesperado ***" in out
    assert "corrieron hacia la casa de" not in out


def test_two_pig_indestructible_houses() -> None:
    blows_limit = 3
    wolf = Wolf(blows_limit=blows_limit)
    pig1 = Pig(
        material="ladrillos",
        personality="el más trabajador",
        house_description="tardó mucho en construirse pero quedó muy sólida.",
        blows_to_fall=None,
    )
    pig2 = Pig(
        material="acero",
        personality="el más más trabajador",
        house_description="tardó muchísimo en construirse pero quedó extremadamente sólida.",
        blows_to_fall=None,
    )
    scenario = Scenario(pigs=[pig1, pig2], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "Había una vez 2 chanchitos" in out
    assert out.count("¡Soplaré y soplaré, y tu casa derribaré!") == blows_limit
    assert out.count("La casa de ladrillos resistió.") == blows_limit
    assert "Al ver que no podía derribarla, el lobo se dio por vencido." in out
    assert (
        "Los chanchitos se quedaron juntos en la casa de ladrillos, contentos y a salvo."
        in out
    )
    assert "corrieron hacia la casa de" not in out


def test_two_pigs_first_falls() -> None:
    blows_limit = 3
    wolf = Wolf(blows_limit=blows_limit)
    pig1 = Pig(
        material="paja",
        personality="el más flojo",
        house_description="se levanta rápido pero es muy frágil.",
        blows_to_fall=1,
    )
    pig2 = Pig(
        material="ladrillos",
        personality="el más trabajador",
        house_description="tardó mucho en construirse pero quedó muy sólida.",
        blows_to_fall=None,
    )
    scenario = Scenario(pigs=[pig1, pig2], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "La casa de paja cayó." in out
    assert "El chanchito corrió hacia la casa de ladrillos." in out
    assert (
        "Los" not in out.split("corrieron", maxsplit=1)[0].split("\n")[-1]
        if "corrieron" in out
        else True
    )
    assert "Los chanchitos corrieron hacia la casa de ladrillos." not in out
    assert (
        "Los chanchitos se quedaron juntos en la casa de ladrillos, contentos y a salvo."
        in out
    )


def test_two_pigs_both_fall() -> None:
    blows_limit = 3
    wolf = Wolf(blows_limit=blows_limit)
    pig1 = Pig(
        material="paja",
        personality="el más flojo",
        house_description="se levanta rápido pero es muy frágil.",
        blows_to_fall=1,
    )
    pig2 = Pig(
        material="madera",
        personality="algo trabajador",
        house_description="se levanta con más trabajo, aunque puede romperse.",
        blows_to_fall=2,
    )
    scenario = Scenario(pigs=[pig1, pig2], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "Había una vez 2 chanchitos" in out
    assert "La casa de paja cayó." in out
    assert "El chanchito corrió hacia la casa de madera." in out
    assert (
        out.count("¡Soplaré y soplaré, y tu casa derribaré!") == 1 + 2
    )  # 1 on paja + 2 on madera
    assert "La casa de madera resistió." in out
    assert "La casa de madera cayó." in out
    assert (
        "Los chanchitos corrieron hacia la casa de" not in out
    )  # no third house to flee to
    assert "*** ERROR: escenario inesperado ***" in out
    assert "contentos y a salvo." not in out
    assert "Entonces el lobo trató de entrar por la chimenea" not in out


def test_three_pigs_two_fall() -> None:
    blows_limit = 3
    wolf = Wolf(blows_limit=blows_limit)
    pig1 = Pig(
        material="paja",
        personality="el más flojo",
        house_description="se levanta rápido pero es muy frágil.",
        blows_to_fall=1,
    )
    pig2 = Pig(
        material="madera",
        personality="algo trabajador",
        house_description="se levanta con más trabajo, aunque puede romperse.",
        blows_to_fall=2,
    )
    pig3 = Pig(
        material="ladrillos",
        personality="el más trabajador",
        house_description="tardó mucho en construirse pero quedó muy sólida.",
        blows_to_fall=None,
    )
    scenario = Scenario(pigs=[pig1, pig2, pig3], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "La casa de paja cayó." in out
    assert "El chanchito corrió hacia la casa de madera." in out
    assert "La casa de madera cayó." in out
    assert "Los chanchitos corrieron hacia la casa de ladrillos." in out
    assert (
        "Los chanchitos se quedaron juntos en la casa de ladrillos, contentos y a salvo."
        in out
    )


def test_ending_contains_chimney_and_moral() -> None:
    wolf = Wolf(blows_limit=3)
    pig = Pig(
        material="ladrillos",
        personality="el más trabajador",
        house_description="tardó mucho en construirse pero quedó muy sólida.",
        blows_to_fall=None,
    )
    scenario = Scenario(pigs=[pig], wolf=wolf)

    lines: list[str] = []
    Narrator(Writer(lines.append)).tell(scenario)

    out = "\n".join(lines)
    assert "Entonces el lobo trató de entrar por la chimenea" in out
    assert "Hacer las cosas con paciencia y esfuerzo" in out
