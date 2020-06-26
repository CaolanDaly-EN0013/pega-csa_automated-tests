'''
This module contains shared fixtures.
'''

import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    # Initialise ChromeDriver instance
    cb = selenium.webdriver.Chrome()

    # Make its calls wait up to 10 seconds for elements to appear
    cb.implicitly_wait(10)

    # Return the WebDriver instance for setup
    yield cb

    cb.quit()