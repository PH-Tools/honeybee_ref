---
DATE: 2026-07-15
STATUS: CANONICAL
---

# honeybee-ref — Tech Stack

## Runtime

- **IronPython 2.7** (loaded into Rhino/Grasshopper via the Honeybee-PH plugins) **and** CPython ≥ 3.10. Source files carry `# -*- Python Version: 2.7 -*-`.

## Dependencies

- Runtime: `honeybee-energy` only.
- Dev extras: `black`, `isort`, `pytest`, `pytest-cov`.

## Packaging

- setuptools + wheel; single package `honeybee_energy_ref`. Published to PyPI as **`honeybee-ref`**.

## Testing

- **pytest** — `python -m pytest` (`testpaths = "tests"`, `python_files = "test_*.py"`). `filterwarnings = ["error", ...]` — warnings are errors.
- Tests cover the reference objects and property serialization (`test_document_ref.py`, `test_image_ref.py`, `test_external_identifier.py`, `test_constructions.py`, `test_materials.py`).

## Formatting

- **Black** + **isort**.

## Versioning & release

- Version lives in `pyproject.toml` `[project] version`. Release is GitHub-driven: publish a GitHub Release → `.github/workflows/ci.yml` builds and deploys to PyPI. (`.github/workflows/tests.yml` also runs pytest.)

## Docs

- No `docs/` folder / docs-hub spoke in this repo.
