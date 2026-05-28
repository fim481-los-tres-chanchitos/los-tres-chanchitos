import argparse
import json
import sys
from pathlib import Path

from rich import print as rich_print

from los_tres_chanchitos import __version__
from los_tres_chanchitos.defaults import original_scenario
from los_tres_chanchitos.models import Pig, Scenario, Wolf
from los_tres_chanchitos.narrator import Narrator
from los_tres_chanchitos.writer import Writer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="los-tres-chanchitos")
    parser.add_argument(
        "--version",
        action="version",
        version=f"los-tres-chanchitos {__version__}",
    )
    parser.add_argument(
        "--scenario",
        metavar="FILE",
        help="Ruta a un archivo JSON con un escenario alternativo.",
    )
    parser.add_argument(
        "--location",
        metavar="NAME",
        help="Ubicación del cuento",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.scenario:
        try:
            scenario = load_scenario_from_file(args.scenario)
        except FileNotFoundError:
            print(
                f"Error: no se encontró el archivo '{args.scenario}'.", file=sys.stderr
            )
            return 1
        except (KeyError, TypeError, json.JSONDecodeError) as e:
            print(f"Error al leer el escenario: {e}", file=sys.stderr)
            return 1
    else:
        scenario = original_scenario()

    writer = Writer(
        rich_print, args.location if args.location is not None else "el bosque"
    )
    narrator = Narrator(writer)
    narrator.tell(scenario)
    return 0


def load_scenario_from_file(path: str) -> Scenario:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    pigs = [Pig(**pig) for pig in data["pigs"]]
    wolf = Wolf(**data["wolf"])
    return Scenario(pigs=pigs, wolf=wolf)
