def handler(event, context):
    orders = event.get("orders", [])
    return {"processed": len(orders)}