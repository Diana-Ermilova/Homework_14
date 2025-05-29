#у Author.Today очень недружелюбный API, поэтому придется использовать дополнительные библиотеки
import pytest
import requests
from bs4 import BeautifulSoup
from config import config
from utils.attach import log_response, attach_response


class ApiAuthorToday:
    def __init__(self):
        self.base_url = config.base_url
        self.session = requests.session()

    def _get_token(self, _id):
        response = self.session.get(self.base_url)
        log_response(response)
        attach_response(response)
        return BeautifulSoup(response.text).find("form", id=_id).find(
            "input", {"name": "__RequestVerificationToken"})['value']

    def is_logged_in(self):
        return {c.name: c.value for c in self.session.cookies}.get('LoginCookie') is not None

    def update_library(self, book_id, state):
        if not self.is_logged_in():
            self.login({"Login": config.login_author_today, "Password": config.pass_author_today})
        token = self._get_token("logoffForm")
        response =  self.session.post(
            self.base_url + 'work/updateLibrary',
            json = {"ids":[book_id], "state": state},
            headers={'requestverificationtoken': token, "x-requested-with": "XMLHttpRequest"})
        log_response(response)
        attach_response(response)
        return response

    def login(self, data):
        login_token = self._get_token("loginForm")

        response =  self.session.post(self.base_url + "account/login",
                                     data={**data, "__RequestVerificationToken": login_token})
        log_response(response)
        attach_response(response)
        return response

    def logout(self):
        logoff_token = self._get_token("logoffForm")
        response = self.session.post(
            self.base_url + "account/logoff",
            data = {"__RequestVerificationToken": logoff_token})
        log_response(response)
        attach_response(response)
        return response

    def send_delete_method(self): #это полностью искусственный тест, так как на AuthorToday в подавляющем большинстве используются GET и POST запросы
        response = self.session.delete(self.base_url + "work/updateLibrary")
        log_response(response)
        attach_response(response)
        return response

api_author_today = ApiAuthorToday()

