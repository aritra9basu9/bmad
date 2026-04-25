# Skill: Maintenance Flaky and Drift

## Purpose
Keep automation stable by identifying flaky behavior and selector drift.

## Signals
- Intermittent pass/fail across repeated runs
- Locator not found spikes
- Increased test duration variance

## Actions
1. Rank tests by flakiness score.
2. Classify likely root cause:
   - timing issue
   - unstable locator
   - environment dependency
3. Propose remediation:
   - explicit waits
   - locator update
   - test data isolation
4. Track status until stable.
