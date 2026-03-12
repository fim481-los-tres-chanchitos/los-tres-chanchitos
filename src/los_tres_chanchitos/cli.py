import argparse

from rich import print as rich_print

from los_tres_chanchitos import __version__
from los_tres_chanchitos.defaults import original_scenario
from los_tres_chanchitos.narrator import Narrator
from los_tres_chanchitos.writer import Writer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="los-tres-chanchitos")
    parser.add_argument(
        "--version",
        action="version",
        version=f"los-tres-chanchitos {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    writer = Writer(rich_print)
    narrator = Narrator(writer)
    narrator.tell(original_scenario())
    return 0
