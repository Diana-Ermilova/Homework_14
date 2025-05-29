import allure
from selene import browser, by, have

class LoginPage():
    def open(self):
        with allure.step("Открытие страницы входа"):
            browser.open('Account/Login')

    def input_login_form(self, login, password):
        with allure.step("Ввод логина и пароля для входа в аккаунт Author Today"):
            browser.element('[name="Login"]').type(text=login)
            browser.element('[name="Password"]').type(text=password)
            browser.element('[class="btn btn-primary btn-block mt-lg"]').click()

