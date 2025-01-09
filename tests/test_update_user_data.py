import allure
import httpx
from jsonschema import validate
from core.contracts import UPDATED_USER_SCHEME
import datetime

BASE_URL = "https://reqres.in/"
UPDATE_USER = "api/users/2"

@allure.suite('Проверка обновления данных пользователя')
@allure.title('Проверяем обновление данных пользователя методом PUT')
def test_update_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step(f'Делаем PUT запрос по адресу: {BASE_URL + UPDATE_USER} с телом {body}'):
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step('Извлекаем JSON-ответ'):
        response_json = response.json()

    with allure.step('Проверяем схему ответа'):
        validate(response_json, UPDATED_USER_SCHEME)

    with allure.step('Проверяем, что имя и работа совпадают с переданными данными'):
        assert response_json['name'] == body['name']
        assert response_json['job'] == body['job']

    with allure.step('Проверяем корректность времени обновления'):
        updated_date = response_json['updatedAt'].replace('T', ' ').split('.')[0]
        current_date = str(datetime.datetime.now(datetime.UTC)).split('.')[0]
        assert updated_date[:16] == current_date[:16]

@allure.suite('Проверка обновления данных пользователя')
@allure.title('Проверяем обновление данных пользователя с использованием PATCH')
def test_patch_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step(f'Делаем запрос на обновление пользователя по адресу: {BASE_URL + UPDATE_USER}'):
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()

    with allure.step('Проверяем корректность обновленных данных'):
        assert response_json['name'] == body['name']
        assert response_json['job'] == body['job']

    with allure.step('Проверяем корректность времени обновления'):
        updated_date = response_json['updatedAt'].replace('T', ' ').split('.')[0]
        current_date = str(datetime.datetime.now(datetime.UTC)).split('.')[0]
        assert updated_date[:16] == current_date[:16]

    validate(response_json, UPDATED_USER_SCHEME)

