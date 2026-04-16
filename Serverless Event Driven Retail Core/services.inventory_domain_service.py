inventory_store = {
    "item_1": {"stock": 50},
    "item_2": {"stock": 20}
}

def update_stock(item_id, quantity):
    inventory_store[item_id]["stock"] -= quantity
    return inventory_store[item_id]["stock"]

def is_low_stock(item_id):
    return inventory_store[item_id]["stock"] < 10