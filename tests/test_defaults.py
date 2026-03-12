from los_tres_chanchitos.defaults import original_scenario


def test_has_three_pigs() -> None:
    scenario = original_scenario()
    assert len(scenario.pigs) == 3


def test_pig_materials() -> None:
    scenario = original_scenario()
    assert [p.material for p in scenario.pigs] == ["paja", "madera", "ladrillos"]


def test_wolf_blows() -> None:
    scenario = original_scenario()
    assert scenario.wolf.blows_limit == 3


def test_blows_to_fall_increasing() -> None:
    scenario = original_scenario()
    assert scenario.pigs[0].blows_to_fall == 1
    assert scenario.pigs[1].blows_to_fall == 2


def test_last_pig_never_falls() -> None:
    scenario = original_scenario()
    assert scenario.pigs[-1].blows_to_fall is None
