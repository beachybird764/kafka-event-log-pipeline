import json
import random
import time
import uuid
from datetime import datetime

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

users = [101, 102, 103, 104, 105]
devices = ["Mobile", "Laptop", "Tablet"]
browsers = ["Chrome", "Firefox", "Edge", "Safari"]
cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Hyderabad"]

actions = [
    "login",
    "logout",
    "search",
    "view_product",
    "add_to_cart",
    "checkout",
    "payment_success",
    "payment_failed"
]

while True:

    event = {
        "event_id": str(uuid.uuid4()),
        "event_time": datetime.utcnow().isoformat(),
        "user_id": random.choice(users),
        "session_id": str(uuid.uuid4())[:8],
        "device": random.choice(devices),
        "browser": random.choice(browsers),
        "city": random.choice(cities),
        "action": random.choice(actions),
        "amount": round(random.uniform(100, 5000), 2),
        "status": random.choice(["SUCCESS", "FAILED"])
    }

    producer.send("event_logs", event)
    producer.flush()

    print(json.dumps(event, indent=4))

    time.sleep(1)