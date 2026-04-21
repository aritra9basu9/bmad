package org.bmad.steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import org.bmad.core.ConfigManager;
import org.bmad.core.DriverFactory;
import org.bmad.pages.HomePage;
import org.testng.Assert;

public class SmokeSteps {
    private HomePage homePage;

    @Given("I open the application home page")
    public void iOpenTheApplicationHomePage() {
        homePage = new HomePage(DriverFactory.getDriver());
        homePage.open(ConfigManager.get("base.url"));
    }

    @Then("the page title should contain {string}")
    public void thePageTitleShouldContain(String expectedText) {
        Assert.assertTrue(
                homePage.getTitle().contains(expectedText),
                "Expected title to contain: " + expectedText + ", actual: " + homePage.getTitle()
        );
    }
}
