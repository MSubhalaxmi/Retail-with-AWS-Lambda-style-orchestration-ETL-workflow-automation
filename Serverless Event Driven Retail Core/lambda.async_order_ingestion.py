import asyncio

async def process_order(order):
    # simulate processing
    return {"id": order["id"], "status": "processed"}

async def handler(event, context):
    orders = event.get("orders", [])
    tasks = [process_order(o) for o in orders]

    results = await asyncio.gather(*tasks)
    return {"processed_count": len(results)}