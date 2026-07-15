# context/ — canonical repo documentation

Stable, ground-truth documentation for honeybee-ref. Distinct from `planning/` (in-flight work). This repo has no `docs/` folder.

`CLAUDE.md` at the repo root is the dispatcher; this folder holds the docs it routes to.

## Index

| Doc | Read when you need… |
|-----|---------------------|
| [`PRD.md`](PRD.md) | What honeybee-ref is for and what belongs here |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | The `_extend`/`properties` pattern and the reference objects |
| [`TECH_STACK.md`](TECH_STACK.md) | Runtime, packaging, testing, CI, release |
| [`CODING_STANDARDS.md`](CODING_STANDARDS.md) | IPy2.7 rules, serialization, testing |

## Maintenance rule

When a change alters the object model or serialization, fold it into the relevant doc here. Keep it true.
