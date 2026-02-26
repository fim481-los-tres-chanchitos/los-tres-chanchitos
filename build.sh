#!/usr/bin/env sh

set -eu
cd "$(dirname "$0")"

QUICK_CHECK=0
for arg in "$@"; do
    case "$arg" in
        --quick-check) QUICK_CHECK=1 ;;
        *) echo "Error: argumento desconocido: $arg" >&2; exit 1 ;;
    esac
done

if [ -z "${VIRTUAL_ENV:-}" ]; then
    echo "Error: virtualenv no activo. Activa .venv antes de ejecutar build.sh" >&2
    exit 1
fi

if [ "$QUICK_CHECK" -eq 0 ]; then
    # Regenera dependencias desde pyproject.toml
    sh ./generate-requirements.sh
    # Instala dependencias necesarias para trabajar
    python -m pip install -r requirements-dev.txt
    # Instala dependencias necesarias para publicar
    python -m pip install -r requirements-release.txt
    # Instala este paquete en modo editable (entry points y metadata)
    python -m pip install -e . --no-deps
fi
python -m ruff format .
python -m ruff check --fix .
python -m ruff format --check .
python -m ruff check .
python -m mypy src/
python -m pylint src/ tests/
python -m pytest --cov-fail-under=80
if [ "$QUICK_CHECK" -eq 0 ]; then
    rm -rf dist build
    python -m build
    python -m twine check dist/*
fi
