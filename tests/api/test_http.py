import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(f"Responce is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('http://api.github.com/users/defunkt')
    # Поміщаємо Значення json файлу у змінну
    body = r.json() 
    # поміщаємо заголовки відповіді у змінну
    headers = r.headers

    # Перевіряємо чи імя дорівнює "Chris Wanstrath"
    assert body['name'] == "Chris Wanstrath" 
    assert body['type'] == "User"
    assert body['company'] == None
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('http://api.github.com/users/serg444iy')
    assert r.status_code == 404