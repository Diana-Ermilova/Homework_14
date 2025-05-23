import allure
from selene import browser, be, have
from allure_commons.types import Severity

from tests import main_page
from tests.main_page import *


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Открытие главной страницы")
@allure.link("https://author.today/", name="Testing")

def main_page_test(setup_browser):
    main_page = MainPage()
    main_page.open()




