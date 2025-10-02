import pytest
from selene import browser


@pytest.fixture()
def setup_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.driver.maximize_window()
    yield
    browser.quit()
