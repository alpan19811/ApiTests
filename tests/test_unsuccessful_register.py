import httpx
import allure
from jsonschema import validate
from core.contracts import UNSUCCESSFUL_REGISTER_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USERS = "api/register"
@allure.suite('Регистрация пользователей')
@allure.title('Проверка ошибки при регистрации без пароля')
def test_unsuccessful_register():
    request_data = {
        "email": "sydney@fife"
    }
    with allure.step('Отправка POST-запроса для регистрации пользователя без пароля'):
        response = httpx.post(BASE_URL + REGISTER_USERS, json=request_data)
    with allure.step('Проверка, что статус ответа равен 400'):
        assert response.status_code == 400, f"Unexpected status code: {response.status_code}, Response: {response.text}"
    with allure.step('Проверка ответа на соответствие JSON-схеме ошибки регистрации'):
        validate(response.json(), UNSUCCESSFUL_REGISTER_SCHEME)
    with allure.step('Проверка сообщения об ошибке в теле ответа'):
        response_data = response.json()
        assert response_data["error"] == "Missing password", f"Unexpected error message: {response_data['error']}"