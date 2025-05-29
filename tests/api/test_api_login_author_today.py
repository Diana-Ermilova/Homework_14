import pytest
import allure
from allure_commons.types import Severity
from bs4 import BeautifulSoup
from jsonschema import validate

from config import config
from models.api_author_today import api_author_today
from schema.schema import unsuccessful_login

data_login = {"Login": config.login_author_today, "Password": config.pass_author_today}
bad_data = {"Login": config.wrong_login, "Password": config.wrong_pass}


@pytest.mark.incremental
class TestAuthorTodayApi:
    @allure.tag('critical')
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "ErmilovaDV")
    @allure.feature("Author Today")
    @allure.story("Неудачный логин на сайт")
    @allure.link("https://author.today/Account/Login", name="Testing")
    def test_unsuccessfull_login(self):
        response = api_author_today.login(bad_data)
        assert response.status_code == 200
        assert response.json()["isSuccessful"] == False
        response_body = response.json()
        validate(response_body, unsuccessful_login)


    @allure.tag('critical')
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "ErmilovaDV")
    @allure.feature("Author Today")
    @allure.story("Удачный логин на сайт")
    @allure.link("https://author.today/Account/Login", name="Testing")
    def test_successful_login(self):
        response = api_author_today.login(data_login)
        assert response.status_code == 200
        assert api_author_today.is_logged_in()

    @allure.tag('critical')
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "ErmilovaDV")
    @allure.feature("Author Today")
    @allure.story("Логаут из аккаунта")
    @allure.link("https://author.today/account/logoff", name="Testing")
    def test_logout(self):
        response = api_author_today.logout()
        assert response.status_code == 200
        assert not api_author_today.is_logged_in()


