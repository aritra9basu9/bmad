# Skill: Architecture Slice Definition

## Purpose
Define implementation slices that can be delivered independently.

## Slice template
- `slice_name`
- `components_in_scope`
- `interfaces/contracts`
- `risks`
- `acceptance_criteria`
- `test_requirements`

## Rules
- Keep each slice independently testable.
- Include observability requirements per slice.
- Include rollback plan for integration slices.
