import allure
from allure_commons.types import Severity
from selene import browser, have, by

from config import config


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Открытие страницы входа на сайт")
@allure.link("https://author.today/Account/Login", name="Testing")
def test_open(author_today_login_page):
    browser.element('[class="authorization-title"]').should(have.text("Войти"))
    browser.element('[class="authorization-title"]').should(have.text("Зарегистрироваться"))

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Заполнение формы логина для входа на сайт")
@allure.link("https://author.today/Account/Login", name="Testing")
def test_input_login_form(author_today_login_page):
    author_today_login_page.input_login_form(config.login_author_today, config.pass_author_today)
    browser.element('[class="avatar"]').hover()
    browser.element('[class="dropdown dropdown-list"]').element(by.text("Выйти"))

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Попытка логина с неверными кредами")
@allure.link("https://author.today/Account/Login", name="Testing")
def test_input_login_form_with_wrong_data(author_today_login_page):
    author_today_login_page.input_login_form(config.wrong_login, config.wrong_pass)
    browser.element('[class="block-center authorization"]').should(have.text("Неверный логин или пароль."))
