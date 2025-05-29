from selene import browser, have, be
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.core.match import browser_has_script_returned

from config import config


class LoginPage:

    def tap_to_remove_popup(self):
        with allure.step("Скипнуть попап на весь экран"):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Открыть список книг Последние обновления")).click()

    def successful_login(self):
        with (allure.step("Успешный логин в аккаунт Author Today")):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="app.author.today.authortoday:id/login_action"]')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="app.author.today.authortoday:id/buttonLogin"]')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="app.author.today.authortoday:id/textEmail"]')).type(text=config.login_author_today)
            browser.element((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="app.author.today.authortoday:id/textInputPassword"]')).type(text=config.pass_author_today)
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="app.author.today.authortoday:id/buttonLogin"]')).click()
            browser.element((AppiumBy.XPATH,
                             '//android.widget.ImageView[@resource-id="app.author.today.authortoday:id/roundActionImage"]')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.RelativeLayout[@content-desc="Сообщения"]')
                            ).should(have.attribute("content-desc", "Сообщения"))

    def unsuccessful_login(self):
        with allure.step("Логин в аккаунт неуспешен"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="app.author.today.authortoday:id/login_action"]')).click()
            browser.element((AppiumBy.XPATH,
                             '//android.widget.Button[@resource-id="app.author.today.authortoday:id/buttonLogin"]')).click()
            browser.element((AppiumBy.XPATH,
                             '//android.widget.EditText[@resource-id="app.author.today.authortoday:id/textEmail"]')).type(
                text=config.wrong_login)
            browser.element((AppiumBy.XPATH,
                             '//android.widget.EditText[@resource-id="app.author.today.authortoday:id/textInputPassword"]')).type(
                text=config.wrong_pass)
            browser.element((AppiumBy.XPATH,
                             '//android.widget.Button[@resource-id="app.author.today.authortoday:id/buttonLogin"]')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="app.author.today.authortoday:id/snackbar_text"]')).should(have.text("Неверное имя пользователя или пароль"))
    def search_book(self):
        with allure.step("Поиск книги по названию"):
            browser.element((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="app.author.today.authortoday:id/ivIcon"])[1]')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="app.author.today.authortoday:id/textSearchInput"]')).type(text="Евангелион")
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="app.author.today.authortoday:id/buttonSearchWithString"]')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Результаты поиска"]')).should(have.text("Результаты поиска"))

login_page = LoginPage()

