from allure_commons.types import Severity
from models.main_page import *
from selene import browser, have


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Открытие главной страницы")
@allure.link("https://author.today/", name="Testing")

def test_main_page(main_page):
    main_page.open()

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Кликабельность кнопки поиска")
@allure.link("https://author.today/", name="Testing")
def test_icon_search(main_page):
    main_page.icon_search()
    browser.element('[class="form-control"]').should(have.attribute("placeholder", "Найти автора, книгу, пост или арт..."))

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Поиск существующих результатов на сайте")
@allure.link("https://author.today/", name="Testing")
def test_positive_search(main_page):
    main_page.positive_search()
    browser.element('[class$="show-all-link"]').should(have.text("показать все"))



@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Листаем категории результатов")
@allure.link("https://author.today/", name="Testing")
def test_chosing_in_existing_results(main_page):
    main_page.positive_search()
    main_page.chosing_in_existing_results()
    browser.element('[class="text-muted mb-lg"]').should(have.text("Результатов:"))



@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Author Today")
@allure.story("Поиск несуществующих результатов на сайте")
@allure.link("https://author.today/", name="Testing")
def test_negative_search(main_page):
    main_page.negative_search()
    browser.element('[class="panel panel-body empty-panel"]').should(have.text("Ваш запрос не дал результатов."))#результат звучит как наличие текста Ваш запрос не дал результатов.





