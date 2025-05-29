import json

import pytest
import allure
from allure_commons.types import Severity

from models.api_author_today import api_author_today
from schema.schema import book_is_not_exist
from jsonschema import validate

response_update_library_success = json.loads('''{
  "isSuccessful": true,
  "isWarning": false,
  "messages": null,
  "data": null
}''')

@pytest.mark.incremental
class TestUpdateLibrary:
    @allure.tag('critical')
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "ErmilovaDV")
    @allure.feature("Author Today")
    @allure.story("Добавление конкретной книги в библиотеку")
    @allure.link("https://author.today/work/updateLibrary", name="Testing")
    def test_add_book(self):
        response = api_author_today.update_library(451706, "Reading")
        assert response.status_code == 200
        assert response.json() == response_update_library_success

    @allure.tag('critical')
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "ErmilovaDV")
    @allure.feature("Author Today")
    @allure.story("Удаление книги из библиотеки")
    @allure.link("https://author.today/work/updateLibrary", name="Testing")
    def test_remove_book(self):
        response = api_author_today.update_library(451706, "None")
        assert response.status_code == 200
        assert response.json() == response_update_library_success

    @allure.tag('critical')
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "ErmilovaDV")
    @allure.feature("Author Today")
    @allure.story("Добавление несуществующей книги в библиотеку")
    @allure.link("https://author.today/work/updateLibrary", name="Testing")
    def test_book_is_not_exist(self):
        response = api_author_today.update_library(3456789045678945678, "Reading")
        #теоретически, можно еще баг-репорт оформить, там вытекает отладочная информация
        assert response.status_code == 200
        assert response.json()["isSuccessful"] == False
        response_body = response.json()
        validate(response_body, book_is_not_exist)

