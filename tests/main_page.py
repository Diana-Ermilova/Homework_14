import allure
from selene import browser, have, be

# тесты главной страницы сайта AuthorToday
class MainPage():
    @allure.step("Открываем главную страницу сайта")
    def open(self):
        browser.open('/')
