from flask import Flask, jsonify, request
from inventory import inventory
from api import get_product_by_barcode

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management System API",
        "author": "Collins Masira",
        "status": "API Running"
    })


# =========================
# CRUD
# =========================

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):

    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory", methods=["POST"])
def add_inventory():

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    required = [
        "barcode",
        "name",
        "category",
        "quantity",
        "price"
    ]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_item = {
        "id": len(inventory) + 1,
        **data
    }

    inventory.append(new_item)

    return jsonify({
        "message": "Inventory item added successfully",
        "item": new_item
    }), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory(item_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    for item in inventory:

        if item["id"] == item_id:

            item["barcode"] = data.get("barcode", item["barcode"])
            item["name"] = data.get("name", item["name"])
            item["category"] = data.get("category", item["category"])
            item["quantity"] = data.get("quantity", item["quantity"])
            item["price"] = data.get("price", item["price"])

            return jsonify({
                "message": "Inventory updated successfully",
                "item": item
            }), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory(item_id):

    for item in inventory:

        if item["id"] == item_id:
            inventory.remove(item)

            return jsonify({
                "message": "Inventory item deleted successfully"
            }), 200

    return jsonify({"error": "Item not found"}), 404


# =========================
# Helper Routes
# =========================

@app.route("/inventory/search")
def search_inventory():

    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Please provide a product name"}), 400

    results = []

    for item in inventory:

        if name.lower() in item["name"].lower():
            results.append(item)

    return jsonify(results), 200


@app.route("/inventory/count")
def inventory_count():

    return jsonify({
        "total_items": len(inventory)
    })


@app.route("/inventory/low-stock")
def low_stock():

    items = []

    for item in inventory:

        if item["quantity"] < 10:
            items.append(item)

    return jsonify(items), 200


# =========================
# External API
# =========================

@app.route("/product/<barcode>", methods=["GET"])
def fetch_product(barcode):

    product = get_product_by_barcode(barcode)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(product), 200


@app.route("/inventory/import/<barcode>", methods=["POST"])
def import_product(barcode):

    product = get_product_by_barcode(barcode)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    new_item = {
        "id": len(inventory) + 1,
        **product
    }

    inventory.append(new_item)

    return jsonify({
        "message": "Product imported successfully",
        "item": new_item
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
