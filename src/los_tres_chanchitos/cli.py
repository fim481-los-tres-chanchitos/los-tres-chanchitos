import argparse

from rich import print as rich_print

from los_tres_chanchitos import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="los-tres-chanchitos")
    parser.add_argument(
        "--version",
        action="version",
        version=f"los-tres-chanchitos {__version__}",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="mundo",
        help="Nombre a saludar (default: mundo)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    rich_print(f"Hola, [green]{args.name}[/green]!")
    return 0
