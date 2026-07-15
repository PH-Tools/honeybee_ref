---
DATE: 2026-07-15
STATUS: CANONICAL
---

# honeybee-ref — Architecture

## Big picture

honeybee-ref is a **Honeybee-Energy extension**. It attaches a `.ref` property slot to Honeybee objects using Honeybee's `properties` extension mechanism, and that data serializes into the standard HBJSON alongside everything else — the same pattern `honeybee_ph` uses.

```
Honeybee-Energy object  ──.properties (ref slot)──►  reference objects  ──to_dict()──►  HBJSON
```

## Modules

- `_extend_honeybee_energy_ref.py` — registers the `.ref` property slot onto the Honeybee object types (runs on import). Importing the package is what wires it up.
- `document_ref.py` — `DocumentReference`: a document URI plus thumbnail and full-size image URIs, with a generated `identifier`.
- `image_ref.py` — image reference objects.
- `properties/hb_obj.py` — the per-host-object property class that owns `to_dict()`/`from_dict()` for the `.ref` data.

## Serialization contract

Reference objects implement `to_dict()`/`from_dict()` (and `duplicate()` where relevant). HBJSON is the interchange format, so **backward compatibility is required**: `from_dict()` must tolerate HBJSON written before a field existed. See `CODING_STANDARDS.md`.

## Constraints

- IPy2.7-safe (loaded into Rhino). Runtime dep: `honeybee-energy` only.
