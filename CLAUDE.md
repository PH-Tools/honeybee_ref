# honeybee-ref

A Honeybee extension that adds a `ref` property slot to Honeybee-Energy objects for tracking **source and reference data** (document URIs, images, external identifiers) attached to Honeybee objects. Published on PyPI as `honeybee-ref`. Source: https://github.com/PH-Tools/honeybee_ref

> **Runtime constraint:** must run under **IronPython 2.7** (it is loaded into Rhino/Grasshopper via the Honeybee-PH plugins) as well as CPython 3.10+. Source files carry a `# -*- Python Version: 2.7 -*-` header. See `context/CODING_STANDARDS.md`.

## What this repo is

A single package, `honeybee_energy_ref`, that layers reference-tracking data onto Honeybee-Energy objects:

- `_extend_honeybee_energy_ref.py` — registers the `.ref` property slot onto Honeybee objects (runs on import).
- `document_ref.py` — `DocumentReference` (document/PDF URIs + thumbnail/full-size image URIs).
- `image_ref.py` — image reference objects.
- `properties/` — the per-host-object property classes that own `to_dict()`/`from_dict()`.

## Where things live — read before working

| Working on… | Read |
|-------------|------|
| Scope, what belongs here | `context/PRD.md` |
| The `_extend`/`properties` pattern, object model | `context/ARCHITECTURE.md` |
| IPy2.7 rules, serialization, testing | `context/CODING_STANDARDS.md` |
| Deps, packaging, CI, release | `context/TECH_STACK.md` |
| Current / in-flight work | `planning/STATUS.md` |

Full context index: `context/README.md`. (This repo has no `docs/` hub spoke.)

## Hard rules

1. **IronPython 2.7 compatibility is mandatory.** No f-strings/`pathlib`/modern stdlib; comment-style type hints; guard `typing` imports. Keep the `# -*- Python Version: 2.7 -*-` header on source files.
2. **Backward-compatible serialization.** New fields get a default in `__init__`, are written in `to_dict()`, read with `_input_dict.get("key", default)` in `from_dict()`, and copied in `duplicate()`. Old HBJSON must still load.
3. **Attach data via the `_extend`/`properties` mechanism**, not by monkey-patching around it.
4. **Verify before closeout:** `python -m pytest`.

## Ecosystem

A small Honeybee-Energy extension consumed by the **honeybee_grasshopper_ph** toolchain (document/reference tracking). Sibling of `honeybee_ph` (same extension pattern).
