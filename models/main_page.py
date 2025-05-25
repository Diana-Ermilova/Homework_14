import allure
from selene import browser, by, have


# тесты главной страницы сайта AuthorToday
class MainPage:
    def open(self):
        with allure.step("Открытие главной страницы https://author.today/"):
            browser.open('/')

    def icon_search(self):
        with allure.step("Кликабельность кнопки поиска"):
            browser.element('[class="icon-search"]').click()

    def positive_search(self):
        with allure.step("Поиск существующих результатов на сайте"):
            browser.element('[class="icon-search"]').click()
            browser.element('[class="form-control"]').type("Евангелион").press_enter()

    def chosing_in_existing_results(self):
        with allure.step("Листаем категории результатов"):
            browser.element('[class="panel sidebar search-sidebar"]').element(by.text("Авторы")).click()
            browser.element('[class="panel sidebar search-sidebar"]').element(by.text("Произведения")).click()
            browser.element('[class="panel sidebar search-sidebar"]').element(by.text("Обсуждения")).click()
            browser.element('[class="panel sidebar search-sidebar"]').element(by.text("Иллюстрации")).click()
            browser.element('[class="panel sidebar search-sidebar"]').element(by.text("Подборки")).click()

    def negative_search(self):
        with allure.step("Поиск несуществующих результатов на сайте"):
            browser.element('[class="icon-search"]').click()
            browser.element('[class="form-control"]').type("hhjghgffghvhvgvghvg").press_enter()




