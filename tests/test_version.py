import importlib.metadata

import los_tres_chanchitos


def test_version_matches_package_metadata() -> None:
    assert los_tres_chanchitos.__version__ == importlib.metadata.version(
        "los-tres-chanchitos"
    )


def test_get_version_fallback(monkeypatch) -> None:
    def raise_not_found(_: str) -> str:
        raise los_tres_chanchitos.PackageNotFoundError()

    monkeypatch.setattr(los_tres_chanchitos, "version", raise_not_found)

    # Acceso intencional a helper interno para validar el fallback cuando no hay metadata.
    # pylint: disable-next=protected-access
    assert los_tres_chanchitos._get_version() == "0.0.0"
