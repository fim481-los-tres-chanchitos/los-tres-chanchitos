from los_tres_chanchitos.models import Pig, Scenario, Wolf, WolfBlow


def _make_pig(blows_to_fall: int | None) -> Pig:
    return Pig(
        material="paja",
        personality="tenía prisa",
        house_description="se levanta rápido.",
        blows_to_fall=blows_to_fall,
    )


# --- Pig / Wolf / Scenario fields ---


def test_pig_fields() -> None:
    pig = Pig(
        material="paja",
        personality="tenía prisa",
        house_description="se levanta rápido, pero es poco resistente.",
        blows_to_fall=1,
    )
    assert pig.material == "paja"
    assert pig.personality == "tenía prisa"
    assert pig.blows_to_fall == 1


def test_pig_never_falls() -> None:
    pig = Pig(
        material="ladrillos",
        personality="paciente",
        house_description="es sólida.",
        blows_to_fall=None,
    )
    assert pig.blows_to_fall is None


def test_scenario_fields() -> None:
    wolf = Wolf(blows_limit=3)
    pig = _make_pig(blows_to_fall=1)
    scenario = Scenario(pigs=[pig], wolf=wolf)
    assert len(scenario.pigs) == 1
    assert scenario.wolf.blows_limit == 3
    assert scenario.pigs[0] is pig


# --- falls_under ---


def test_falls_when_blows_reach_threshold() -> None:
    assert _make_pig(blows_to_fall=2).falls_under(wolf_blows=2)


def test_falls_when_blows_exceed_threshold() -> None:
    assert _make_pig(blows_to_fall=1).falls_under(wolf_blows=3)


def test_does_not_fall_when_blows_below_threshold() -> None:
    assert not _make_pig(blows_to_fall=3).falls_under(wolf_blows=2)


def test_never_falls_when_blows_to_fall_is_none() -> None:
    assert not _make_pig(blows_to_fall=None).falls_under(wolf_blows=100)


# --- Scenario.iterate_wolf_visits ---


def _make_scenario(*blows: int | None) -> Scenario:
    return Scenario(
        pigs=[
            Pig(
                material=f"material{i}",
                personality="",
                house_description="",
                blows_to_fall=b,
            )
            for i, b in enumerate(blows)
        ],
        wolf=Wolf(blows_limit=3),
    )


def test_attack_sequence_yields_one_entry_per_pig() -> None:
    scenario = _make_scenario(1, 2, None)
    assert len(list(scenario.iterate_wolf_visits())) == 3


def test_attack_sequence_pigs_in_current_house_accumulates() -> None:
    scenario = _make_scenario(1, 2, None)
    counts = [visit.pigs_in_current_house for visit in scenario.iterate_wolf_visits()]
    assert counts == [1, 2, 3]


def test_attack_sequence_next_pig_is_none_for_last() -> None:
    scenario = _make_scenario(1, None)
    entries = list(scenario.iterate_wolf_visits())
    assert entries[-1].next_pig is None


def test_attack_sequence_next_pig_is_correct() -> None:
    scenario = _make_scenario(1, 2, None)
    entries = list(scenario.iterate_wolf_visits())
    assert entries[0].next_pig is scenario.pigs[1]
    assert entries[1].next_pig is scenario.pigs[2]


def test_attack_sequence_current_pig_is_correct() -> None:
    scenario = _make_scenario(1, 2, None)
    entries = list(scenario.iterate_wolf_visits())
    assert entries[0].current_pig is scenario.pigs[0]
    assert entries[1].current_pig is scenario.pigs[1]
    assert entries[2].current_pig is scenario.pigs[2]


# --- Scenario.iterate_wolf_blows ---


def test_wolf_blows_yields_range_from_1_to_limit() -> None:
    scenario = _make_scenario(1, 2, None)
    assert list(scenario.iterate_wolf_blows()) == [
        WolfBlow(1),
        WolfBlow(2),
        WolfBlow(3),
    ]


def test_wolf_blows_single_blow() -> None:
    scenario = Scenario(pigs=[], wolf=Wolf(blows_limit=1))
    assert list(scenario.iterate_wolf_blows()) == [WolfBlow(1)]


def test_wolf_blows_zero_limit_is_empty() -> None:
    scenario = Scenario(pigs=[], wolf=Wolf(blows_limit=0))
    assert not list(scenario.iterate_wolf_blows())
