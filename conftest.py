import pytest
from selene import browser
from selenium.webdriver import ChromeOptions

from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="128.0",
    )


@pytest.fixture(scope="function")
def setup_browser(request):
    browser_version = request.config.getoption("--browser_version")
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {"enableVideo": True, "enableVNC": True})

    browser.config.driver_remote_url = (
        "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    )
    browser.config.driver_options = options
    browser.config.base_url = "https://demoqa.com"
    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
