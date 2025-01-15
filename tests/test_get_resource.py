import re
import httpx
from jsonschema import validate
from core.contracts import RESOURCE_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
SINGLE_RESOURCE_NOT_FOUND = "api/unknown/23"
COLOR_START = "#"
PANTONE_VALUE_MASK = r"^\d{2}-\d{4}$" # Регулярное выражение для формата "NN-NNNN"
YEAR_MASK = r"^\d{4}$" # Регулярное выражение для формата "YYYY"
@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение списка ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step(f'Проверяем данные ресурса: {item}'):
            validate(item, RESOURCE_SCHEME)
            with allure.step('Проверяем, что поле color начинается с "#"'):
                assert item['color'].startswith(COLOR_START)
            with allure.step('Проверяем формат pantone_value'):
                assert re.match(PANTONE_VALUE_MASK, item['pantone_value'])
            with allure.step('Проверяем формат года'):
                assert re.match(YEAR_MASK, str(item['year']))

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение одного ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    with allure.step('Проверяем данные ресурса'):
        with allure.step('Проверяем, что поле color начинается с "#"'):
            assert data['color'].startswith(COLOR_START)
        with allure.step('Проверяем формат года'):
            assert re.match(YEAR_MASK, str(data['year']))

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем ресурс, который не существует')
def test_resource_not_found():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_RESOURCE_NOT_FOUND}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE_NOT_FOUND)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404