from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Event:
    event_id: str
    event_timestamp: str

    application_id: str
    application_version: str

    device_id: str
    device_type: str
    device_model: str
    os_version: str

    user_id: str
    session_id: str

    event_type: str
    screen_name: str

    product_id: Optional[str]
    product_name: Optional[str]
    category: Optional[str]
    brand: Optional[str]

    price: Optional[float]
    quantity: Optional[int]

    payment_status: Optional[str]

    country: str
    state: str
    city: str

    ip_address: str

    network_type: str

    browser: Optional[str]

    response_time_ms: int

    status: str

    error_code: Optional[str]
    error_message: Optional[str]

    ingestion_source: str

    schema_version: str

    def to_dict(self):
        return asdict(self)

