#у Author.Today очень недружелюбный API, поэтому придется использовать дополнительные библиотеки
import pytest
import requests
from bs4 import BeautifulSoup
from config import config

class ApiAuthorToday:
    def __init__(self):
        self.base_url = config.base_url
        self.session = requests.session()

    def _get_token(self, _id):
        response = self.session.get(self.base_url)
        return BeautifulSoup(response.text).find("form", id=_id).find(
            "input", {"name": "__RequestVerificationToken"})['value']

    def is_logged_in(self):
        return {c.name: c.value for c in self.session.cookies}.get('LoginCookie') is not None

    def update_library(self, book_id, state):
        if not self.is_logged_in():
            self.login({"Login": config.login_author_today, "Password": config.pass_author_today})
        token = self._get_token("logoffForm")
        return self.session.post(
            self.base_url + 'work/updateLibrary',
            json = {"ids":[book_id], "state": state},
            headers={'requestverificationtoken': token, "x-requested-with": "XMLHttpRequest"})

    def login(self, data):
        login_token = self._get_token("loginForm")

        return self.session.post(self.base_url + "account/login",
                                     data={**data, "__RequestVerificationToken": login_token})

    def logout(self):
        logoff_token = self._get_token("logoffForm")
        return self.session.post(
            self.base_url + "account/logoff",
            data = {"__RequestVerificationToken": logoff_token})





api_author_today = ApiAuthorToday()

