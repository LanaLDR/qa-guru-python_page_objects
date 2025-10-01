import pytest
from selene import browser

@pytest.fixture()
def setup_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()