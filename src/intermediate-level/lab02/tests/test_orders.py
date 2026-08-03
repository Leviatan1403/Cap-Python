from conftest import client


def get_token():
    response = client.post("/login", json={"username": "admin", "password": "admin123"})

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def test_crear_order():
    headers = get_token()

    response = client.post(
        "/orders/",
        json={"customer": "Juan", "product": "Laptop", "quantity": 2},
        headers=headers,
    )

    assert response.status_code == 201


def test_obtener_orders():
    headers = get_token()

    response = client.get("/orders/", headers=headers)

    assert response.status_code == 200


def test_actualizar_order():
    headers = get_token()

    response = client.put(
        "/orders/1",
        json={
            "customer": "Juan",
            "product": "Mouse",
            "quantity": 5,
            "status": "Completed",
        },
        headers=headers,
    )

    assert response.status_code == 200


def test_eliminar_order():
    headers = get_token()

    response = client.delete("/orders/1", headers=headers)

    assert response.status_code == 204
