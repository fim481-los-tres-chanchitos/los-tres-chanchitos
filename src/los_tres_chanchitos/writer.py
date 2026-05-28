from collections.abc import Callable

from los_tres_chanchitos.models import Pig


class Writer:
    def __init__(self, writer: Callable[[str], None]) -> None:
        self._writer = writer

    def intro(self, pig_count: int) -> None:
        noun = "chanchito" if pig_count == 1 else "chanchitos"
        self._writer(
            f"Había una vez {pig_count} {noun} que decidieron construir sus propias casas "
            "para vivir con tranquilidad en el bosque.\n"
        )

    def building(self, pig: Pig, pig_number: int) -> None:
        self._writer(f"El chanchito {pig_number}, {pig.personality}, dijo:\n")
        self._writer(f"— Ya lo decidí: haré mi casa de {pig.material}.\n")
        self._writer("— Me pondré a trabajar ahora mismo.\n")
        self._writer(f"Una casa de {pig.material} {pig.house_description}\n")

    def wolf_arrives(self) -> None:
        self._writer("Un día apareció un lobo hambriento.\n")

    def wolf_knocks(self, pig: Pig, blow_number: int) -> None:
        if blow_number == 1:
            self._writer(
                f"El lobo fue a la casa de {pig.material}, golpeó la puerta y dijo:\n"
            )
        else:
            self._writer("El lobo golpeó la puerta otra vez y dijo:\n")

    def wolf_threatens_and_blows(self, blow_number: int) -> None:
        self._writer("— ¡Soplaré y soplaré, y tu casa derribaré!\n")
        if blow_number == 1:
            self._writer("Y sopló con fuerza.\n")
        else:
            self._writer(f"Y sopló por {blow_number}ª vez.\n")

    def house_resists(self, pig: Pig) -> None:
        self._writer(f"La casa de {pig.material} resistió.\n")

    def house_falls(self, pig: Pig) -> None:
        self._writer(f"La casa de {pig.material} cayó.\n")

    def pigs_flee(self, pigs_in_current_house: int, next_pig: Pig) -> None:
        if pigs_in_current_house == 1:
            self._writer(f"El chanchito corrió hacia la casa de {next_pig.material}.\n")
        else:
            self._writer(
                f"Los chanchitos corrieron hacia la casa de {next_pig.material}.\n"
            )

    def house_survives(self) -> None:
        self._writer("Al ver que no podía derribarla, el lobo se dio por vencido.\n")

    def ending(self, surviving_pig: Pig) -> None:
        self._writer(
            "Entonces el lobo trató de entrar por la chimenea. Pero los chanchitos "
            "encendieron el fuego de la estufa y pusieron una olla con agua. Al sentir "
            "el calor, el lobo se asustó, salió corriendo y no volvió.\n"
        )
        self._writer(
            f"Los chanchitos se quedaron juntos en la casa de "
            f"{surviving_pig.material}, contentos y a salvo.\n"
        )
        self._writer(
            "Hacer las cosas con paciencia y esfuerzo suele dar mejores resultados "
            "que hacerlo con apuro.\n"
        )

    def error(self) -> None:
        self._writer("*** ERROR: escenario inesperado ***\n")
