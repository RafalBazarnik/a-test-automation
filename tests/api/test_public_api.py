import requests


def test_get_public_api(settings):
    response = requests.get(f"{settings.api_base_url}/todos/1", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
