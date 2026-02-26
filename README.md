# Los tres chanchitos

Proyecto para jugar con Git.

## Requisitos

- Python 3.10+

## Setup (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -e . --no-deps
```

## Setup (Linux / macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install -e . --no-deps
```

## Actualizar lock de dependencias

```bash
sh ./generate-requirements.sh
```

Se generan 3 archivos:

- `requirements.txt` (runtime/base)
- `requirements-dev.txt` (tooling de desarrollo, incluye runtime/base)
- `requirements-release.txt` (tooling de build/publicación, incluye runtime/base)

## Ejecutar

```bash
python -m los_tres_chanchitos --help
python -m los_tres_chanchitos FIM481

# o vía script instalado
los-tres-chanchitos --version
los-tres-chanchitos FIM481
```

## Formateo y lint

```bash
python -m ruff format .
python -m ruff check .
```

## Tests

```bash
python -m pytest
```

## Release (build)

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -r requirements-release.txt
python -m pip install -e . --no-deps

# construir sdist + wheel en dist/
python -m build

# validar metadata/render del README
python -m twine check dist/*
```

Ver pasos sugeridos en `RELEASE.md`.

## Docker

```bash
docker build -t los-tres-chanchitos .
docker run --rm los-tres-chanchitos
docker run --rm los-tres-chanchitos FIM481
docker run --rm los-tres-chanchitos --version
```
