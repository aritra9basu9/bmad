# BMAD Java Selenium Starter

Starter automation project for your BMAD lifecycle stories using:
- Java 17
- Selenium WebDriver
- Cucumber (Gherkin)
- TestNG
- Maven

## Run tests
```powershell
cd automation-java-selenium
mvn test
```

## Where to add new story scripts
- Feature files: `src/test/resources/features`
- Step definitions: `src/test/java/org/bmad/steps`
- Page objects: `src/test/java/org/bmad/pages`

Use story/test-script IDs as tags in feature files:
- Example: `@S3_04 @TS-S3-04-001`

## Suggested mapping from your backlog
- `S3-01` to `S3-05`: add gherkin + selenium step definitions first.
- `S4-01` to `S4-03`: add CI and defect integration tests (API/integration).
- `S4-05`: add UI dashboard tests under a dedicated feature file.

## Notes
- Default `base.url` is `https://www.selenium.dev`.
- Update `src/test/resources/config.properties` for your app URL.
