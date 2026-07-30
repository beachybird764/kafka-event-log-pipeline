APPLICATION_IDS = [
    "SHOP_APP",
    "SAMSUNG_PAY",
    "SMARTTHINGS",
    "GALAXY_STORE"
]

EVENT_TYPES = [
    "APP_OPEN",
    "LOGIN",
    "SEARCH",
    "PRODUCT_VIEW",
    "ADD_TO_CART",
    "CHECKOUT",
    "PAYMENT_SUCCESS",
    "PAYMENT_FAILED",
    "LOGOUT"
]

DEVICE_TYPES = [
    "Mobile",
    "Tablet",
    "Smart TV",
    "Wearable"
]

DEVICE_CATALOG = {

    "Mobile": [
        "Galaxy S24",
        "Galaxy S24+",
        "Galaxy S24 Ultra",
        "Galaxy S23",
        "Galaxy S23 Ultra",
        "Galaxy Z Fold6",
        "Galaxy Z Flip6"
    ],

    "Tablet": [
        "Galaxy Tab S10",
        "Galaxy Tab S10+"
    ],

    "Wearable": [
        "Galaxy Watch Ultra",
        "Galaxy Watch7"
    ],

    "Smart TV": [
        "Neo QLED 8K",
        "Crystal UHD TV"
    ]
}

CATEGORIES = [
    "Mobile",
    "Tablet",
    "Wearable",
    "TV",
    "Accessories"
]

BRANDS = [
    "Samsung"
]

PRODUCT_PRICE_RANGE = {
    "Mobile": (30000, 120000),
    "Tablet": (20000, 90000),
    "TV": (25000, 250000),
    "Wearable": (5000, 50000),
    "Accessories": (500, 15000)
}

PRODUCT_CATALOG = {
    "Mobile": [
        ("Galaxy S24", 74999),
        ("Galaxy S24+", 84999),
        ("Galaxy S24 Ultra", 129999),
        ("Galaxy Z Fold6", 164999),
        ("Galaxy Z Flip6", 109999)
    ],

    "Tablet": [
        ("Galaxy Tab S10", 69999),
        ("Galaxy Tab S10+", 89999)
    ],

    "Wearable": [
        ("Galaxy Watch Ultra", 59999),
        ("Galaxy Watch7", 32999)
    ],

    "TV": [
        ("Neo QLED 8K", 249999),
        ("Crystal UHD TV", 64999)
    ],

    "Accessories": [
        ("Galaxy Buds3 Pro", 19999),
        ("45W Charger", 2999),
        ("SmartTag2", 3499)
    ]
}

PRODUCT_EVENTS = {
    "PRODUCT_VIEW",
    "ADD_TO_CART",
    "CHECKOUT",
    "PAYMENT_SUCCESS",
    "PAYMENT_FAILED"
}

APPLICATION_EVENT_MAPPING = {

    "SHOP_APP": [
        "APP_OPEN",
        "LOGIN",
        "SEARCH",
        "PRODUCT_VIEW",
        "ADD_TO_CART",
        "CHECKOUT",
        "PAYMENT_SUCCESS",
        "PAYMENT_FAILED",
        "LOGOUT"
    ],

    "SAMSUNG_PAY": [
        "APP_OPEN",
        "LOGIN",
        "PAYMENT_SUCCESS",
        "PAYMENT_FAILED",
        "LOGOUT"
    ],

    "SMARTTHINGS": [
        "APP_OPEN",
        "LOGIN",
        "SEARCH",
        "LOGOUT"
    ],

    "GALAXY_STORE": [
        "APP_OPEN",
        "LOGIN",
        "SEARCH",
        "PRODUCT_VIEW",
        "LOGOUT"
    ]
}

NETWORK_TYPES = [
    "WiFi",
    "4G",
    "5G"
]

PAYMENT_STATUS = [
    "SUCCESS",
    "FAILED",
    "PENDING"
]

EVENT_STATUS = [
    "SUCCESS",
    "FAILED"
]

BROWSERS = [
    "Chrome",
    "Edge",
    "Samsung Internet",
    "Firefox"
]

STATE_CITY_MAPPING = {
    "Karnataka": [
        "Bengaluru",
        "Mysuru"
    ],

    "Maharashtra": [
        "Mumbai",
        "Pune"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Coimbatore"
    ],

    "Telangana": [
        "Hyderabad",
        "Warangal"
    ],

    "Uttar Pradesh": [
        "Noida",
        "Lucknow"
    ]
}

COUNTRIES = [
    "India"
]