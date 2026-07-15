---
DATE: 2026-07-15
STATUS: CANONICAL ENGINEERING STANDARD
---

# honeybee-ref — Coding Standards

## 1. IronPython 2.7 compatibility (mandatory)

Loaded into Rhino/Grasshopper — must run under IronPython 2.7 and CPython 3.10+.

- No f-strings — use `.format()`. No `pathlib`/modern-stdlib-only features.
- Comment-style type hints (`# type: (str) -> dict`), not inline annotations.
- Guard `typing` imports (`try: from typing import ... except ImportError: pass`).
- Keep the `# -*- Python Version: 2.7 -*-` header on source files.

## 2. Backward-compatible serialization

Reference objects round-trip through HBJSON. When adding a field:

1. Add it in `__init__` with a default.
2. Write it in `to_dict()`.
3. Read it in `from_dict()` with `_input_dict.get("key", default)` — never bare `[...]` access.
4. Copy it in `duplicate()` where present.

Old HBJSON without the key must still load.

## 3. Use the `_extend`/`properties` mechanism

Attach the `.ref` data through Honeybee's `properties` extension API (registered in `_extend_honeybee_energy_ref.py`); the property class in `properties/` owns the serialization. Don't bypass this.

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
