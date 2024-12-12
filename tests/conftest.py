import pytest
import selenium.webdriver
import selenium.webdriver.chrome


@pytest.fixture
def browser():
    # initialliCze browser
    browser = selenium.webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
