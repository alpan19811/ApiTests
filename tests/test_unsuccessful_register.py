import httpx
from jsonschema import validate
from core.contracts import UNSUCCESSFUL_REGISTER_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USERS = "api/register"

def test_unsuccessful_register():
    request_data = {
        "email": "sydney@fife"
    }

    response = httpx.post(BASE_URL + REGISTER_USERS, json=request_data)

    assert response.status_code == 400, f"Unexpected status code: {response.status_code}, Response: {response.text}"

    validate(response.json(), UNSUCCESSFUL_REGISTER_SCHEME)

    response_data = response.json()
    assert response_data["error"] == "Missing password", f"Unexpected error message: {response_data['error']}"