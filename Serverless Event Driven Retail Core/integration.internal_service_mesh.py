import requests

def call_inventory_service(item_id, qty):
    return requests.post(
        "http://inventory-service/update",
        json={"item_id": item_id, "qty": qty}
    ).json()

def call_pricing_service(data):
    return requests.post(
        "http://pricing-service/calculate",
        json=data
    ).json()