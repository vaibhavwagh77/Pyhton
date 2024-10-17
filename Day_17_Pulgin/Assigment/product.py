import csv
product_inventory = {}
def add_product(product_inventory, product_id, product_name, price, quantity):
    product_inventory[product_id] = (product_name, price, quantity)
    print(f"Product '{product_name}' added successfully!")
def update_quantity(product_inventory, product_id, new_quantity):
    if product_id in product_inventory:
        product_name, price, _ = product_inventory[product_id]
        product_inventory[product_id] = (product_name, price, new_quantity)
        print(f"Updated quantity for Product ID {product_id} to {new_quantity}.")
    else:
        print("Product not found.")
def display_products(product_inventory):
    print("Product Inventory:")
    print(f"{'Product ID'} {'Name'} {'Price'} {'Quantity'}")
    for product_id, (product_name, price, quantity) in product_inventory.items():
        print(f"{product_id} {product_name} {price} {quantity}")



def save_to_csv(product_inventory, filename="product_inventory.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product ID", "Product Name", "Price", "Quantity", "Total Price"])
        for product_id, (product_name, price, quantity) in product_inventory.items():
            total_price = price * quantity
            writer.writerow([product_id, product_name, price, quantity, total_price])
    print(f"Inventory saved to {filename} successfully!")
add_product(product_inventory, "1   ", "   Sugar   ",   100, 2)
add_product(product_inventory, "2   ", "   Wheat   ", 25, 45)
update_quantity(product_inventory, "10", 8)
display_products(product_inventory)
save_to_csv(product_inventory)
