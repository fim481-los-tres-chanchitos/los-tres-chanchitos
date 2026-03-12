from collections.abc import Iterator
from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Pig:
    material: str
    personality: str
    house_description: str
    blows_to_fall: int | None  # None = never falls

    def falls_under(self, wolf_blows: int) -> bool:
        """Returns True if the house falls given the wolf's number of blows."""
        return self.blows_to_fall is not None and self.blows_to_fall <= wolf_blows


@dataclass
class Wolf:
    blows_limit: int  # number of blows before the wolf gives up


class NumberedPig(NamedTuple):
    number: int
    pig: Pig


class WolfVisit(NamedTuple):
    current_pig: Pig
    pigs_in_current_house: int
    next_pig: Pig | None


class WolfBlow(NamedTuple):
    number: int


@dataclass
class Scenario:
    pigs: list[Pig]
    wolf: Wolf

    def iterate_pigs(self) -> Iterator[NumberedPig]:
        for index, pig in enumerate(self.pigs):
            yield NumberedPig(number=index + 1, pig=pig)

    def iterate_wolf_visits(self) -> Iterator[WolfVisit]:
        for visit_number, current_pig in enumerate(self.pigs):
            pigs_in_current_house = visit_number + 1
            next_pig = (
                self.pigs[visit_number + 1]
                if visit_number + 1 < len(self.pigs)
                else None
            )
            yield WolfVisit(current_pig, pigs_in_current_house, next_pig)

    def iterate_wolf_blows(self) -> Iterator[WolfBlow]:
        for blow_number in range(1, self.wolf.blows_limit + 1):
            yield WolfBlow(number=blow_number)
