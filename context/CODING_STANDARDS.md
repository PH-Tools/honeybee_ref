---
DATE: 2026-07-15
STATUS: CANONICAL ENGINEERING STANDARD
---

# honeybee-ref — Coding Standards

## 1. IronPython 2.7 compatibility (mandatory)

The generic dual-runtime rules (banned syntax and modules, comment-style type
hints, guarded `typing` imports, defensive third-party imports, and the lint
settings they imply) live in the **ironpython-27-compatibility** skill. Apply it
before editing anything on the Rhino load path. Only this repo's specifics are
recorded below.

Loaded into Rhino/Grasshopper. The whole package is on the load path.

Keep the `# -*- Python Version: 2.7 -*-` header on source files.

## 2. Backward-compatible serialization

The HBJSON round-trip contract (four steps for a new field, when `.get()` is
required, mutable constructor ownership, `duplicate()` recursion) and the
`_extend`/`properties` attachment mechanism live in the
**hbjson-serialization-contract** skill. Apply it before adding or changing any
field on a model class.

Reference objects round-trip through HBJSON. `duplicate()` exists on some
`honeybee_ref` objects but not all; copy new fields there where it is present.

## 3. Use the `_extend`/`properties` mechanism


The `.ref` data attaches through Honeybee's `properties` extension API,
registered in `_extend_honeybee_energy_ref.py`. The property class in
`properties/` owns the serialization.

## 4. Formatting

- **Black** + **isort**.

## 5. Testing

- **pytest** — `python -m pytest`. Warnings are errors (`filterwarnings = ["error", ...]`).
- New objects/fields need test coverage (serialization round-trip especially).

## Closeout checklist

- [ ] IPy2.7-safe (no f-strings/pathlib; guarded `typing`; comment-style hints; 2.7 header kept).
- [ ] New fields follow the backward-compatible serialization pattern.
- [ ] `python -m pytest` passes (no warnings).
- [ ] black + isort clean.
