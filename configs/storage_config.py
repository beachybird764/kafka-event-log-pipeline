from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data"

LANDING_PATH = str(DATA_PATH / "landing")
BRONZE_PATH = str(DATA_PATH / "bronze")
SILVER_PATH = str(DATA_PATH / "silver")
GOLD_PATH = str(DATA_PATH / "gold")

CHECKPOINT_PATH = str(DATA_PATH / "checkpoints")
LANDING_CHECKPOINT = str(DATA_PATH / "checkpoints" / "landing")