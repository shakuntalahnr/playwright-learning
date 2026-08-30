import pytest
import json
import os
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def config_data():
    config_path = os.path.join("config", "config.json")
    with open(config_path) as config_file:
        return json.load(config_file)

@pytest.fixture(scope="session")
def launch_browser(browser_type):
    """Launch browser with 2-second delay on every action"""
    def launch(**kwargs):
        kwargs.setdefault('slow_mo', 2000)  # 2-second delay
        return browser_type.launch(**kwargs)
    return launch

@pytest.fixture(autouse=True)
def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

def login_page(page, config_data):
    return LoginPage(page, config_data["base_url"])



