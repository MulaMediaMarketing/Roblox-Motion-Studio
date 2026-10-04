# Coding Standards

## Principles

- Explicit dependencies.
- Small cohesive modules.
- Pure domain math where practical.
- No business logic in UI components.
- No direct API calls from presentation components.
- Validate data at boundaries.
- Prefer typed schemas over ad-hoc dictionaries.
- Avoid hidden mutable global state.

## File size

Preferred: under 1,000 lines.
Hard ceiling: 1,200 lines unless documented and approved.

If a file grows toward the limit, split by responsibility rather than by arbitrary line count.

## Naming

Use descriptive names. Avoid abbreviations unless they are industry-standard:
- R15
- GLTF
- API
- FPS
- VFX

## Errors

Errors should identify:
- operation
- relevant resource
- safe diagnostic context

Do not expose secrets, tokens, filesystem credentials, or internal stack traces to users.

## Tests

Core motion math, retargeting, schema validation, interpolation, blending, and exporters require automated tests.

## Git

Use conventional commit style:
- feat:
- fix:
- refactor:
- test:
- docs:
- chore:

Keep commits small and logically reversible.
