import allure
from models.mobile_author_today import login_page

@allure.epic("Mobile, Логин в аккаунт Author Today")
@allure.label("owner", 'ErmilovaDV')
@allure.feature("Неуспешный логин в аккаунт")
@allure.tag('mobile')
@allure.severity('critical')
def test_unsuccessful_login():
    login_page.tap_to_remove_popup()
    login_page.unsuccessful_login()

@allure.epic("Mobile, Логин в аккаунт Author Today")
@allure.label("owner", 'ErmilovaDV')
@allure.feature("Успешный логин в аккаунт")
@allure.tag('mobile')
@allure.severity('critical')
def test_successful_login():
    login_page.tap_to_remove_popup()
    login_page.successful_login()

@allure.epic("Mobile, Логин в аккаунт Author Today")
@allure.label("owner", 'ErmilovaDV')
@allure.feature("Успешный логин в аккаунт")
@allure.tag('mobile')
@allure.severity('critical')
def test_search_book():
    login_page.tap_to_remove_popup()
    login_page.successful_login()
    login_page.search_book()
