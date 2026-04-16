import redis

r = redis.Redis(host="localhost", port=6379)

CHANNEL = "retail-live-updates"

def publish_update(event):
    r.publish(CHANNEL, str(event))

def subscribe_updates(callback):
    pubsub = r.pubsub()
    pubsub.subscribe(CHANNEL)

    for msg in pubsub.listen():
        if msg["type"] == "message":
            callback(msg["data"])