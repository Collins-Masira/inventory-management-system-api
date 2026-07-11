from app import app


def test_get_all_inventory():
    client = app.test_client()
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_item():
    client = app.test_client()
    response = client.post("/inventory", json={
        "barcode": "1111111111111",
        "name": "Test Item",
        "category": "Test",
        "quantity": 5,
        "price": 99
    })
    assert response.status_code == 201
    assert response.get_json()["item"]["name"] == "Test Item"


def test_create_item_missing_field():
    client = app.test_client()
    response = client.post("/inventory", json={"name": "Incomplete"})
    assert response.status_code == 400


def test_get_single_item_not_found():
    client = app.test_client()
    response = client.get("/inventory/99999")
    assert response.status_code == 404


def test_update_item():
    client = app.test_client()
    created = client.post("/inventory", json={
        "barcode": "2222222222222",
        "name": "Update Me",
        "category": "Test",
        "quantity": 1,
        "price": 10
    }).get_json()["item"]

    response = client.patch(f"/inventory/{created['id']}", json={"quantity": 50})
    assert response.status_code == 200
    assert response.get_json()["item"]["quantity"] == 50


def test_delete_item():
    client = app.test_client()
    created = client.post("/inventory", json={
        "barcode": "3333333333333",
        "name": "Delete Me",
        "category": "Test",
        "quantity": 1,
        "price": 10
    }).get_json()["item"]

    response = client.delete(f"/inventory/{created['id']}")
    assert response.status_code == 200

    follow_up = client.get(f"/inventory/{created['id']}")
    assert follow_up.status_code == 404
