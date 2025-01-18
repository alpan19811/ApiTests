import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
SINGLE_USER_NOT_FOUND = "api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"
DELAYED_REQUEST = "api/users?delay=3"

@allure.suite('Проверка запросов данных пользователей') # сьют - это общее название отчета по совокупности тестов/сьюту тестов
@allure.title('Проверяем получение списка пользователей') # тайтл - это название отчета непосредственно для теста
def test_list_users():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_USERS}'): # это шаги...т.е. пояснение сути непосредственно для шага запроса по адресу BASE_URL + LIST_USERS
        response = httpx.get(BASE_URL + LIST_USERS)

    with allure.step('Проверяем код ответа'): # это шаги...т.е. пояснение сути непосредственно для шага проверки кода ответа 200
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step(f'Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание Email адреса'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step('Проверяем наличие id в ссылке на аватарку'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение данных одного пользователя')
def test_single_user():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверка кода ответа'):
        assert response.status_code == 200
    with allure.step('Извлекаем данные пользователя'):
        data = response.json()['data']
    with allure.step('Извлекаем окончание Email адреса'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем наличие id в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем пользователя, который не найден')
def test_user_not_found():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_USER_NOT_FOUND}'):
        response = httpx.get(BASE_URL + SINGLE_USER_NOT_FOUND)
    with allure.step('Проверка кода ответа'):
        assert response.status_code == 404

def test_delayed_user_list():
    response = httpx.get(BASE_URL + DELAYED_REQUEST, timeout=5)
    assert response.status_code == 200

