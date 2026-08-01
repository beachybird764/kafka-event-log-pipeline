from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data"

# Landing / Bronze / Silver
LANDING_PATH = str(DATA_PATH / "landing")
BRONZE_PATH = str(DATA_PATH / "bronze")
SILVER_PATH = str(DATA_PATH / "silver")

# Gold Base Path
GOLD_PATH = DATA_PATH / "gold"

# Gold Tables
DIM_APPLICATION_PATH = str(GOLD_PATH / "dim_application")
DIM_DEVICE_PATH = str(GOLD_PATH / "dim_device")
DIM_PRODUCT_PATH = str(GOLD_PATH / "dim_product")
DIM_LOCATION_PATH = str(GOLD_PATH / "dim_location")
DIM_DATE_PATH = str(GOLD_PATH / "dim_date")
DIM_USER_PATH = str(GOLD_PATH / "dim_user")
DIM_SESSION_PATH = str(GOLD_PATH / "dim_session")
FACT_EVENTS_PATH = str(GOLD_PATH / "fact_events")

# Checkpoints
CHECKPOINT_PATH = str(DATA_PATH / "checkpoints")
INGESTION_CHECKPOINT = str(DATA_PATH / "checkpoints" / "landing")

# Audit
AUDIT_PATH = str(DATA_PATH / "audit" / "pipeline_audit")