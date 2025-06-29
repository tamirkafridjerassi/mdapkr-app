import requests

def test_get_people():
    response = requests.get("http://localhost:8000/people")
    assert response.status_code == 200
