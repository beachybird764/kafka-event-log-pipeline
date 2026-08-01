import random
import uuid
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

def generate_uuid() -> str:
    return str(uuid.uuid4())


def generate_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def generate_session_id() -> str:
    return f"SES{uuid.uuid4().hex[:10].upper()}"


def generate_device_id() -> str:
    return f"DEV{random.randint(100000, 999999)}"


def generate_user_id() -> str:
    return f"USR{random.randint(100000, 999999)}"


def generate_product_id() -> str:
    return f"PRD{random.randint(100000, 999999)}"


def generate_ip_address():

    return fake.ipv4()


def generate_response_time() -> int:
    return random.randint(50, 1000)


# to test the above function works smoothly

# if __name__ == "__main__":
#
#     print(generate_uuid())
#     print(generate_timestamp())
#     print(generate_session_id())
#     print(generate_device_id())
#     print(generate_user_id())
#     print(generate_product_id())
#     print(generate_ip_address())
#     print(generate_response_time())

# Run: python utils/generators.py