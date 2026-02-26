# Release

Checklist mínima para construir y publicar el paquete.

## 1. Bump de versión

Editar el campo `version` en `pyproject.toml`.

> Nota: `los_tres_chanchitos.__version__` se obtiene desde metadata del paquete instalado, así que no hay que tocar el código.

## 2. Descargar dependencias

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -r requirements-release.txt
python -m pip install -e . --no-deps
```

## 3. Validación local

```bash
python -m ruff format --check .
python -m ruff check .
python -m pytest
```

## 4. Construir artefactos

```bash
python -m build
python -m twine check dist/*
```

## 5. Publicar

### PyPI

```bash
python -m twine upload dist/*
```

### TestPyPI (opcional)

```bash
python -m twine upload --repository testpypi dist/*
```

## 6. Tag (opcional)

```bash
git tag -a vX.Y.Z -m "vX.Y.Z"
git push --tags
```
