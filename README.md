# Inventory Management System API

A Flask-based REST API for managing inventory in a small retail business. The application allows administrators to create, read, update, and delete inventory items while integrating with the OpenFoodFacts API to retrieve real-time product information.

---

## Project Overview

This project was developed as part of the **Moringa School Software Engineering Program**.

The system enables users to:

* View inventory items
* Add new inventory items
* Update existing inventory items
* Delete inventory items
* Search inventory by product name
* View total inventory count
* View low-stock items
* Fetch product information from the OpenFoodFacts API
* Import products directly into the inventory
* Interact with the API through a Command Line Interface (CLI)

---

## Technologies Used

* Python 3.11
* Flask
* Requests
* Pytest
* Git & GitHub

---

## Project Structure

```
inventory-management-system-api/
│
├── app.py
├── api.py
├── cli.py
├── inventory.py
├── requirements.txt
├── README.md
├── tests/
│   ├── test_routes.py
│   ├── test_crud.py
│   ├── test_external_api.py
│   └── test_cli.py
└── data/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Collins-Masira/inventory-management-system-api.git
```

Navigate into the project:

```bash
cd inventory-management-system-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Flask Application

```bash
python app.py
```

The application runs at:

```
http://127.0.0.1:5000
```

---

## API Endpoints

| Method | Endpoint                    | Description                      |
| ------ | ---------------------------- | -------------------------------- |
| GET    | /                             | Home Route                       |
| GET    | /inventory                    | Get all inventory                |
| GET    | /inventory/`<id>`             | Get one inventory item           |
| POST   | /inventory                    | Add inventory item               |
| PATCH  | /inventory/`<id>`             | Update inventory item            |
| DELETE | /inventory/`<id>`             | Delete inventory item            |
| GET    | /inventory/search?name=       | Search inventory                 |
| GET    | /inventory/count              | Count inventory                  |
| GET    | /inventory/low-stock          | Low-stock items                  |
| GET    | /product/`<barcode>`          | Fetch product from OpenFoodFacts |
| POST   | /inventory/import/`<barcode>` | Import product into inventory    |

---

## Command Line Interface

Run the CLI (with the Flask app running in a separate terminal):

```bash
python cli.py
```

Available options:

* View Inventory
* View Item
* Add Item
* Update Item
* Delete Item
* Search Product (OpenFoodFacts)
* Import Product (OpenFoodFacts)
* Exit

---

## Running Tests

Run the full test suite:

```bash
pytest tests/ -v
```

Example output:

```
======================== test session starts ========================
collected 16 items

tests/test_cli.py::test_display_menu_prints_options PASSED
tests/test_cli.py::test_view_inventory_calls_api_and_prints PASSED
tests/test_crud.py::test_get_all_inventory PASSED
tests/test_crud.py::test_create_item PASSED
tests/test_crud.py::test_create_item_missing_field PASSED
tests/test_crud.py::test_get_single_item_not_found PASSED
tests/test_crud.py::test_update_item PASSED
tests/test_crud.py::test_delete_item PASSED
tests/test_external_api.py::test_fetch_product_found PASSED
tests/test_external_api.py::test_fetch_product_not_found PASSED
tests/test_external_api.py::test_import_product_adds_to_inventory PASSED
tests/test_routes.py::test_home_route PASSED
tests/test_routes.py::test_search_requires_name PASSED
tests/test_routes.py::test_search_finds_match PASSED
tests/test_routes.py::test_inventory_count PASSED
tests/test_routes.py::test_low_stock PASSED

======================== 16 passed in 0.29s =========================
```

---

## Git Workflow

Development was split across three feature branches, each opened as its own
pull request into `main`, reviewed, merged, and deleted after merging:

| Branch | What it added |
|---|---|
| `feature/crud-and-routing` | Full CRUD routes, plus search/count/low-stock helper routes, plus the external API routes in `app.py` |
| `feature/external-api-cli` | `api.py` (OpenFoodFacts integration) and `cli.py` (the interactive command-line client) |
| `feature/testing` | The full pytest suite (`tests/`) |

Workflow used for each feature:

```bash
git checkout main
git pull
git checkout -b feature/<name>
# ...work, commit...
git push -u origin feature/<name>
# Open a Pull Request on GitHub (base: main <- compare: feature/<name>)
# Review, then click "Merge pull request", then "Delete branch"
git checkout main
git pull
```

All three branches were merged in this order — `crud-and-routing` →
`external-api-cli` → `testing` — with no merge conflicts, since each branch
touched a distinct set of files.

---

## Features Implemented

* RESTful Flask API
* CRUD Operations
* Search functionality
* Low-stock reporting
* Inventory counting
* External API integration
* CLI application
* Automated testing with Pytest (16 tests)
* Git branching workflow: 3 feature branches, each merged via its own pull request

---

## Future Improvements

* Database integration (SQLite or PostgreSQL)
* User authentication
* Product image support
* Pagination
* Inventory analytics dashboard

---

## Author

**Collins Masira**

Moringa School Software Engineering Student

GitHub: https://github.com/Collins-Masira

---

## License

This project is for educational purposes as part of the Moringa School Software Engineering Program.