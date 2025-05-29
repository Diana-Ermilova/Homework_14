import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from models.author_today_login_page import LoginPage
from models.main_page import MainPage
from utils.attach import *
from config import config

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def main_page():
    page = MainPage()
    page.open()
    return page

@pytest.fixture(scope='function')
def author_today_login_page():
    page = LoginPage()
    page.open()
    return page


@pytest.fixture(autouse=True, scope='function')
def setup_browser():
    browser.config.base_url = config.base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1500
    browser.config.timeout = 10.0

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    if config.run_in_selenoid:
        executor = f"https://{config.selenoid_login}:{config.selenoid_pass}@{config.selenoid_url}/wd/hub"
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "127.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=executor,
            options=options)
        browser.config.driver = driver

    yield
    add_video(browser)
    add_logs(browser)
    add_screenshot(browser)
    add_html(browser)
    browser.quit()

