# Skill: Security Scan Gate

## Purpose
Evaluate vulnerability and quality scan outcomes before release.

## Policy model
- `critical`: block
- `high`: block unless approved override
- `medium`: warn and track
- `low`: informational

## Steps
1. Collect scanner outputs.
2. Normalize findings to a common severity model.
3. Apply policy thresholds.
4. Emit gate decision:
   - pass
   - fail
   - pass-with-override
