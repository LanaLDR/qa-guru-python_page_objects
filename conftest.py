import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver import ChromeOptions

from utils import attach

DEFAULT_BROWSER_VERSION = "128.0"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="128.0",
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {"enableVideo": True, "enableVNC": True})

    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    browser.config.driver_remote_url = (
        f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub"
    )
    browser.config.driver_options = options
    browser.config.base_url = "https://demoqa.com"
    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
