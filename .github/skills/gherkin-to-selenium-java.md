# Skill: Gherkin to Selenium Java

## Purpose
Generate executable Java Selenium automation from approved feature files.

## Project target
- `automation-java-selenium/`

## Steps
1. Write `.feature` files with story/test IDs as tags.
2. Add step definitions under `src/test/java/org/bmad/steps`.
3. Add/extend page objects under `src/test/java/org/bmad/pages`.
4. Keep environment settings in `src/test/resources/config.properties`.
5. Validate with `mvn test`.

## Quality gates
- No hard-coded sleeps if avoidable.
- Locators centralized in page objects.
- Assertions must map to acceptance criteria.
- Failing tests must output actionable evidence.
