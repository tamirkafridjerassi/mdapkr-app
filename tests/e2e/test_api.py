# tests/e2e/test_api.py

import requests
import time

def wait_for_api(url, timeout=30):
    for _ in range(timeout):
        try:
            res = requests.get(url)
            if res.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    return False

def test_get_people():
    url = "http://localhost:8000/people"
    assert wait_for_api(url), "API not reachable"
    response = requests.get(url)
    assert response.status_code == 200
