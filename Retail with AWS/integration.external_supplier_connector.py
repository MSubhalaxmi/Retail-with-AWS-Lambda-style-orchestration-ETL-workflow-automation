import requests

def fetch_supplier_data():
    res = requests.get("https://api.supplier.com/data")
    return res.json()