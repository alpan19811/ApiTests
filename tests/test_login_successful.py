import json
import allure
import httpx
import pytest
from jsonschema import validate
from core.contracts import LOGIN_SUCCESSFUL_SCHEME

BASE_URL = "https://reqres.in/"
LOGIN_USERS = "api/login"

json_file = open('C:/Users/User/PycharmProjects/ApiTests/core/login_successful_data.json') #обращаемся к json-файлу
users_data = json.load(json_file) #загружаем json-файл
@allure.suite('Проверка авторизации пользователей')
@allure.title('Успешная авторизация пользователя')
@pytest.mark.parametrize('users_data', users_data) #параметризация по "users_data"
def test_successful_login(users_data):
    with allure.step('Отправка POST-запроса для авторизации пользователя'):
        response = httpx.post(BASE_URL + LOGIN_USERS, json=users_data)
    with allure.step('Проверка, что статус ответа равен 200'):
        assert response.status_code == 200
    with allure.step('Проверка ответа на соответствие JSON-схеме успешной авторизации'):
        validate(response.json(), LOGIN_SUCCESSFUL_SCHEME)