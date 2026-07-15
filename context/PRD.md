---
DATE: 2026-07-15
STATUS: CANONICAL PRD
---

# honeybee-ref — Product Requirements

## 1. Goal

Let users attach **source and reference data** — document URIs (PDFs, spec sheets), images, and external identifiers — to Honeybee-Energy objects, so a Honeybee model can carry provenance/evidence alongside its energy data. This matters for Passive House certification workflows where every input should be justified by a source document.

## 2. Who uses it

- The **honeybee_grasshopper_ph** toolchain, at runtime in Rhino/Grasshopper (IronPython 2.7).
- Python users of Honeybee-Energy who want a `.ref` slot (`pip install honeybee-ref`).

## 3. What belongs here

- The `.ref` property slot on Honeybee-Energy objects (via the `_extend` mechanism).
- The reference objects: `DocumentReference` (document + thumbnail/full-size image URIs), image references, external identifiers.
- Their `to_dict()`/`from_dict()` HBJSON serialization (in `properties/`).

## 4. Non-goals

- **No document storage or fetching.** honeybee-ref stores *URIs/references*, not the files themselves.
- **No UI.** Any Grasshopper components live in the plugin repos.
- **No heavy dependencies** — it must stay IPy2.7-safe and loadable in Rhino.

## 5. Success criteria

- A model with `.ref` data round-trips losslessly through HBJSON, including old HBJSON without the newer keys.
- Loads and runs under IronPython 2.7.
- Tests cover the reference objects and the property serialization.

## 6. Direction

- Active work (if any) tracked in `planning/STATUS.md`.
