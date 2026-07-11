import requests

BASE_URL = "http://127.0.0.1:5000"


def display_menu():
    print("\n" + "=" * 45)
    print(" INVENTORY MANAGEMENT SYSTEM ")
    print("=" * 45)
    print("1. View Inventory")
    print("2. View One Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Search Product (OpenFoodFacts)")
    print("7. Import Product from OpenFoodFacts")
    print("8. Exit")


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print("\nInventory:")
    print(response.json())


def view_one_item():
    item_id = input("Enter Item ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    print(response.json())


def add_item():

    barcode = input("Barcode: ")
    name = input("Name: ")
    category = input("Category: ")

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
    except ValueError:
        print("\nQuantity must be a whole number and price must be numeric.")
        return

    data = {
        "barcode": barcode,
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )

    print(response.json())


def update_item():

    item_id = input("Item ID: ")

    print("\nLeave fields blank if you don't want to change them.\n")

    barcode = input("Barcode: ")
    name = input("Name: ")
    category = input("Category: ")
    quantity = input("Quantity: ")
    price = input("Price: ")

    data = {}

    if barcode:
        data["barcode"] = barcode

    if name:
        data["name"] = name

    if category:
        data["category"] = category

    if quantity:
        data["quantity"] = int(quantity)

    if price:
        data["price"] = float(price)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    print(response.json())


def delete_item():

    item_id = input("Item ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    print(response.json())


def search_product():

    barcode = input("Barcode: ")

    response = requests.get(
        f"{BASE_URL}/product/{barcode}"
    )

    print(response.json())


def import_product():

    barcode = input("Barcode: ")

    response = requests.post(
        f"{BASE_URL}/inventory/import/{barcode}"
    )

    print(response.json())


def main():

    while True:

        display_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_one_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            search_product()

        elif choice == "7":
            import_product()

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
