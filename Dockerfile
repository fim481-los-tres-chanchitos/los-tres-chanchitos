FROM python:3.13-slim AS test

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE requirements-dev.txt ./
COPY src ./src
COPY tests ./tests

RUN python -m pip install --no-cache-dir -r requirements-dev.txt \
    && python -m pip install --no-cache-dir -e . --no-deps \
    && python -m ruff format --check . \
    && python -m ruff check . \
    && python -m pytest

FROM test AS builder

COPY requirements-release.txt ./requirements-release.txt

RUN python -m pip install --no-cache-dir -r requirements-release.txt \
    && python -m build \
    && python -m twine check dist/*

FROM python:3.13-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home --shell /usr/sbin/nologin appuser

COPY requirements.txt ./requirements.txt
COPY --from=builder /app/dist/*.whl /tmp/
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir --no-deps /tmp/*.whl \
    && rm -rf /tmp/*.whl

USER appuser

ENTRYPOINT ["los-tres-chanchitos"]
CMD ["mundo"]
