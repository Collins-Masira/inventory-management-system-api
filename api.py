import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

HEADERS = {
    "User-Agent": "InventoryManagementSystem/1.0 (Moringa School Project)"
}


def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data["product"]

        return {
            "barcode": barcode,
            "name": product.get("product_name", "Unknown Product"),
            "category": product.get("categories", "Unknown"),
            "quantity": 10,
            "price": 0
        }

    except requests.exceptions.RequestException:
        return None
