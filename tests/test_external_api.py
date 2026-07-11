from unittest.mock import patch
from app import app


def _mock_response(status_code=200, status=1, product=None):
    class MockResponse:
        def __init__(self):
            self.status_code = status_code

        def json(self):
            return {"status": status, "product": product or {}}
    return MockResponse()


def test_fetch_product_found():
    client = app.test_client()
    with patch("api.requests.get", return_value=_mock_response(
        product={"product_name": "Nutella", "categories": "Spreads"}
    )):
        response = client.get("/product/3017624010701")
        assert response.status_code == 200
        assert response.get_json()["name"] == "Nutella"


def test_fetch_product_not_found():
    client = app.test_client()
    with patch("api.requests.get", return_value=_mock_response(status=0)):
        response = client.get("/product/0000000000000")
        assert response.status_code == 404


def test_import_product_adds_to_inventory():
    client = app.test_client()
    with patch("api.requests.get", return_value=_mock_response(
        product={"product_name": "Imported Snack", "categories": "Snacks"}
    )):
        response = client.post("/inventory/import/4444444444444")
        assert response.status_code == 201
        assert response.get_json()["item"]["name"] == "Imported Snack"

        listing = client.get("/inventory").get_json()
        assert any(i["name"] == "Imported Snack" for i in listing)
