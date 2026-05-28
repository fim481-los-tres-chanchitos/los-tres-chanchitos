from los_tres_chanchitos.models import Pig, Scenario
from los_tres_chanchitos.writer import Writer


class Narrator:
    def __init__(self, writer: Writer) -> None:
        self._writer = writer

    def tell(self, scenario: Scenario) -> None:
        """Narrates the full story corresponding to the scenario."""
        self._writer.intro(len(scenario.pigs))

        for entry in scenario.iterate_pigs():
            self._writer.building(entry.pig, entry.number)

        self._writer.wolf_arrives()

        surviving_pig = self._tell_wolf_visits_and_find_surviving_pig(scenario)

        if surviving_pig is None:
            self._writer.error()
            return

        self._writer.ending(surviving_pig, len(scenario.pigs))

    def _tell_wolf_visits_and_find_surviving_pig(
        self, scenario: Scenario
    ) -> Pig | None:
        """Narrates the wolf's visits. Returns the surviving pig or None."""
        for visit in scenario.iterate_wolf_visits():
            house_fell = self._tell_house_attack_and_check_if_fell(
                scenario, visit.current_pig
            )
            if not house_fell:
                self._writer.house_survives()
                return visit.current_pig

            self._writer.house_falls(visit.current_pig)
            if visit.next_pig:
                self._writer.pigs_flee(visit.pigs_in_current_house, visit.next_pig)

        return None

    def _tell_house_attack_and_check_if_fell(
        self, scenario: Scenario, pig: Pig
    ) -> bool:
        """Narrates the attack blow by blow. Returns True if the house fell."""
        for blow in scenario.iterate_wolf_blows():
            self._writer.wolf_knocks(pig, blow.number)
            self._writer.wolf_threatens_and_blows(blow.number)

            if pig.falls_under(blow.number):
                return True

            self._writer.house_resists(pig)

        return False
