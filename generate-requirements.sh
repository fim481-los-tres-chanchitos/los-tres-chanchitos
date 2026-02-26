#!/usr/bin/env sh

set -eu
cd "$(dirname "$0")"

if [ -z "${VIRTUAL_ENV:-}" ]; then
    echo "Error: virtualenv no activo. Activa .venv antes de ejecutar build.sh" >&2
    exit 1
fi

python -m pip install -U pip pip-tools
python -m piptools compile --strip-extras pyproject.toml -o requirements.txt
python -m piptools compile --strip-extras pyproject.toml --extra dev -o requirements-dev.txt
python -m piptools compile --strip-extras pyproject.toml --extra release -o requirements-release.txt
