import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME
import datetime
import allure

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"

@allure.suite('Тесты создания пользователей')
@allure.title('Создание пользователей с именем и должностью')

def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step("Отправляем POST-запрос для создания пользователя"):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step("Проверка, что код ответа равен 201"):
        assert response.status_code == 201

    with allure.step("Проверяем содержимое ответа"):
        response_json = response.json()
        creation_date = response_json['createdAt'].replace('T', ' ')
        current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATED_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]


@allure.suite('Тесты создания пользователей')
@allure.title('Создание пользователя без имени')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }

    with allure.step("Отправляем POST-запрос для создания пользователя"):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step("Проверка, что код ответа равен 201"):
        assert response.status_code == 201

    with allure.step("Проверяем содержимое ответа"):
        response_json = response.json()
        creation_date = response_json['createdAt'].replace('T', ' ')
        current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATED_USER_SCHEME)
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

@allure.suite('Тесты создания пользователей')
@allure.title('Создание пользователя без должности')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step("Отправляем POST-запрос для создания пользователя"):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step("Проверка, что код ответа равен 201"):
        assert response.status_code == 201

    with allure.step("Проверяем содержимое ответа"):
        response_json = response.json()
        creation_date = response_json['createdAt'].replace('T', ' ')
        current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATED_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert creation_date[0:16] == current_date[0:16]