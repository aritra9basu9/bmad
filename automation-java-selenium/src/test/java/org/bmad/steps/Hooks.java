package org.bmad.steps;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import org.bmad.core.DriverFactory;

public class Hooks {
    @Before
    public void setUp() {
        DriverFactory.initDriver();
    }

    @After
    public void tearDown() {
        DriverFactory.quitDriver();
    }
}
