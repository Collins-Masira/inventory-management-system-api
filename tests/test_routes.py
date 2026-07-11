from app import app


def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "API Running"


def test_search_requires_name():
    client = app.test_client()
    response = client.get("/inventory/search")
    assert response.status_code == 400


def test_search_finds_match():
    client = app.test_client()
    response = client.get("/inventory/search?name=cola")
    assert response.status_code == 200
    results = response.get_json()
    assert any("cola" in item["name"].lower() for item in results)


def test_inventory_count():
    client = app.test_client()
    response = client.get("/inventory/count")
    assert response.status_code == 200
    assert "total_items" in response.get_json()


def test_low_stock():
    client = app.test_client()
    response = client.get("/inventory/low-stock")
    assert response.status_code == 200
    for item in response.get_json():
        assert item["quantity"] < 10
