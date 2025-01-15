import allure
import httpx

BASE_URL = "https://reqres.in/"
DELETE_USER = "api/users/2"

@allure.suite('Проверка удаления данных пользователя')
@allure.title('Проверяем удаление пользователя')

def test_delete_user():
    with allure.step(f'Делаем запрос на удаление пользователя по адресу: {BASE_URL + DELETE_USER}'):
        response = httpx.delete(BASE_URL + DELETE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204