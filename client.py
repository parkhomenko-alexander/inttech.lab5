import json
import requests


class Client:

    def __init__(self, login: str, pas: str, url: str):
        self.user_atr = {
            'login': login,
            'pas': pas
        }
        self.BASIC_URL = url

    def __repr__(self):
        return '<login = {} for testing api = {}>'.format(
            self.user_atr['login'], self.BASIC_URL)

    def login(self):
        response = requests.post(
            self.BASIC_URL+'user', data=self.user_atr)
        self.cookies = {'access_token_cookie': dict(
            response.cookies)['access_token_cookie']}

        return self.cookies

    def post_todo(self, descr: str):
        response = requests.post(self.BASIC_URL+'todo',
                                 data={'description': descr}, cookies=self.cookies)
        return response.text

    def get_todo(self):
        response = requests.get(self.BASIC_URL+'todo', cookies=self.cookies)
        todo_list = (json.dumps(response.json(), sort_keys=True,
                     ensure_ascii=False, indent=4))
        return todo_list

    def put_todo(self, id: int, descr: str):
        response = requests.put(
            self.BASIC_URL+f'todo/{id}', data={'description': descr}, cookies=self.cookies)
        return response.text

    def delete_todo(self, id: int):
        response = requests.delete(
            self.BASIC_URL+f'todo/{id}', cookies=self.cookies)
        return response.text
