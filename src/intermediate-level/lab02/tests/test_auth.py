from conftest import client


def test_login_correcto():
    response = client.post("/login", json={"username": "admin", "password": "admin123"})

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_incorrecto():
    response = client.post("/login", json={"username": "admin", "password": "123456"})

    assert response.status_code == 401
