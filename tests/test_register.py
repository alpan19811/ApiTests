import json
import allure
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME


BASE_URL = "https://reqres.in/"
REGISTER_USERS = "api/register"

json_file = open('C:/Users/User/PycharmProjects/ApiTests/core/login_successful_data.json') #обращаемся к json-файлу
users_data = json.load(json_file) #загружаем json-файл
@allure.suite('Проверка регистрации')
@allure.title('Успешная регистрация пользователя')
@pytest.mark.parametrize('users_data', users_data) #параметризация по "users_data"
def test_successful_register(users_data):
    with allure.step('Отправка post-запроса для регистрации пользователя'):
        response = httpx.post(BASE_URL + REGISTER_USERS, json=users_data)
    with allure.step('Проверяем, что код ответа равен 200'):
        assert response.status_code == 200
    with allure.step('Проверяем ответ на соответствие JSON-схеме'):
        validate(response.json(), REGISTERED_USER_SCHEME)

