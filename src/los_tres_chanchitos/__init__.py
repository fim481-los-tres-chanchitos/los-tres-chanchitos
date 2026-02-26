from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]


def _get_version() -> str:
    try:
        return version("los-tres-chanchitos")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = _get_version()
