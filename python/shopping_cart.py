
cart = []


def add_item(name, quantity, price):
    cart.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })


def remove_item(name):
    global cart
    cart = [item for item in cart if item["name"] != name]


def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item in cart:
            print(f"{item['quantity']}x {item['name']} @ {item['price']} each")


def get_total():
    return sum(item["quantity"] * item["price"] for item in cart)

# Example usage
add_item("Laptop", 1, 15000)
add_item("Mouse", 2, 350)
view_cart()
print("Total: R", get_total())

remove_item("Mouse")
view_cart()
print("Total after removing Mouse: R", get_total())