import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from appium import webdriver
from config import config, bstack_config
from utils.attach import *


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="local_real_device",
        help="Specify the test context"
    )

@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = UiAutomator2Options()
    options.set_capability('appWaitActivity', config.android_wait_activity)
    if context == "bstack":
        options.set_capability('app', bstack_config.app)
        options.set_capability('deviceName', bstack_config.device_name)
        options.set_capability('platformName', bstack_config.platform_name)
        options.set_capability('platformVersion', bstack_config.platform_version)
        options.set_capability(
            'bstack:options', {
                'projectName': 'Author Today autotests',
                'buildName': 'AT-Build',
                'sessionName': 'AT-Run',
                'userName': bstack_config.username,
                'accessKey': bstack_config.access_key,
            },
        )
        remote_url = bstack_config.remote_url
    elif context == 'local_real_device':
        options.set_capability('app', os.path.join(os.path.abspath(os.curdir), config.apk_path))
        options.set_capability('deviceName', config.device_name)
        remote_url = config.android_remote_url

    options.set_capability('remote_url', remote_url)
    browser.config.driver = webdriver.Remote(remote_url, options=options)

    browser.config.timeout = 10.0
    session_id = browser.driver.session_id

    yield

    if context =='bstack':
        add_video(browser)
    add_logs(browser, log_type='logcat')
    add_screenshot(browser)

    browser.quit()
