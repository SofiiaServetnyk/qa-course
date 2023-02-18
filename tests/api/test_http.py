import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"The response is: {r.text}")


@pytest.mark.http
def test_second_request():
    request = requests.get('https://api.github.com/users/defunkt')
    body = request.json()
    assert request.status_code == 200
    assert body['name'] == 'Chris Wanstrath'
    assert request.headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    request = requests.get("https://api.github.com/users/some_user")
    assert request.status_code == 404
