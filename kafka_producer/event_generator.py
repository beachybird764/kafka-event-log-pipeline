from models.event import Event
from typing import Dict, Any
import random

from utils.generators import (
    generate_uuid,
    generate_timestamp,
    generate_session_id,
    generate_device_id,
    generate_user_id,
    generate_product_id,
    generate_ip_address,
    generate_response_time
)

from constants.application_constants import (
    APPLICATION_IDS,
    DEVICE_TYPES,
    DEVICE_CATALOG,
    PRODUCT_CATALOG,
    PRODUCT_EVENTS,
    APPLICATION_EVENT_MAPPING,
    NETWORK_TYPES,
    BROWSERS,
    STATE_CITY_MAPPING
)

def generate_application():

    application_id = random.choice(APPLICATION_IDS)

    return {

        "application_id": application_id,

        "application_version":
            f"{random.randint(1,5)}."
            f"{random.randint(0,9)}."
            f"{random.randint(0,9)}"
    }

def generate_device():

    device_type = random.choice(DEVICE_TYPES)

    device_model = random.choice(
        DEVICE_CATALOG[device_type]
    )

    return {
        "device_id": generate_device_id(),
        "device_type": device_type,
        "device_model": device_model,
        "os_version": f"Android {random.randint(11,16)}"
    }

def generate_user() -> Dict[str, str]:
    return {
        "user_id": generate_user_id(),
        "session_id": generate_session_id()
    }

def generate_location() -> Dict[str, str]:

    state = random.choice(list(STATE_CITY_MAPPING.keys()))

    city = random.choice(
        STATE_CITY_MAPPING[state]
    )

    return {
        "country": "India",
        "state": state,
        "city": city
    }

def generate_product() -> Dict[str, Any]:

    category = random.choice(
        list(PRODUCT_CATALOG.keys())
    )

    product_name, base_price = random.choice(
        PRODUCT_CATALOG[category]
    )

    price = round(
        random.uniform(
            base_price * 0.90,
            base_price * 1.10
        ),
        2
    )

    return {
        "product_id": generate_product_id(),
        "category": category,
        "product_name": product_name,
        "brand": "Samsung",
        "price": price,
        "quantity": random.randint(1, 5)
    }

def generate_network() -> Dict[str, str]:
    return {
        "network_type": random.choice(NETWORK_TYPES),
        "browser": random.choice(BROWSERS)
    }


def generate_status(event_type: str) -> Dict[str, Any]:

    if event_type == "PAYMENT_SUCCESS":
        return {
            "status": "SUCCESS",
            "payment_status": "SUCCESS",
            "error_code": None,
            "error_message": None
        }

    if event_type == "PAYMENT_FAILED":
        return {
            "status": "FAILED",
            "payment_status": "FAILED",
            "error_code": "ERR500",
            "error_message": "Payment Failed"
        }

    success = random.random() < 0.90

    if success:
        return {
            "status": "SUCCESS",
            "payment_status": None,
            "error_code": None,
            "error_message": None
        }

    return {
        "status": "FAILED",
        "payment_status": None,
        "error_code": "ERR500",
        "error_message": "Internal Server Error"
    }

def generate_screen_name(event_type):

    mapping = {
        "APP_OPEN": "SplashScreen",
        "LOGIN": "LoginScreen",
        "SEARCH": "SearchScreen",
        "PRODUCT_VIEW": "ProductDetailsScreen",
        "ADD_TO_CART": "CartScreen",
        "CHECKOUT": "CheckoutScreen",
        "PAYMENT_SUCCESS": "PaymentScreen",
        "PAYMENT_FAILED": "PaymentScreen",
        "LOGOUT": "ProfileScreen"
    }

    return mapping.get(event_type, "HomeScreen")

def generate_event():

    application = generate_application()

    event_type = random.choice(
        APPLICATION_EVENT_MAPPING[
            application["application_id"]
        ]
    )

    device = generate_device()
    user = generate_user()
    location = generate_location()
    network = generate_network()
    event_status = generate_status(event_type)

    if event_type in PRODUCT_EVENTS:

        product = generate_product()

        product_id = product["product_id"]
        product_name = product["product_name"]
        category = product["category"]
        brand = product["brand"]
        price = product["price"]
        quantity = product["quantity"]

    else:

        product_id = None
        product_name = None
        category = None
        brand = None
        price = None
        quantity = None

    return Event(
        event_id=generate_uuid(),
        event_timestamp=generate_timestamp(),

        application_id=application["application_id"],
        application_version=application["application_version"],

        device_id=device["device_id"],
        device_type=device["device_type"],
        device_model=device["device_model"],
        os_version=device["os_version"],

        user_id=user["user_id"],
        session_id=user["session_id"],

        event_type=event_type,
        screen_name=generate_screen_name(event_type),

        product_id=product_id,
        product_name=product_name,
        category=category,
        brand=brand,
        price=price,
        quantity=quantity,

        payment_status=event_status["payment_status"],

        country=location["country"],
        state=location["state"],
        city=location["city"],

        ip_address=generate_ip_address(),

        network_type=network["network_type"],
        browser=network["browser"],

        response_time_ms=generate_response_time(),

        status=event_status["status"],

        error_code=event_status["error_code"],
        error_message=event_status["error_message"],

        ingestion_source="Kafka",

        schema_version="1.0"
    )


# if __name__ == "__main__":
#
#     event = generate_event()
#
#     print(event)
#
#     print()
#
#     print(event.to_dict())