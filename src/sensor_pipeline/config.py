
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"
LOG_LEVEL = "INFO"


SENSOR_THRESHOLDS = {
    "sensor1": {
        "max_invalid_ration": 0.1,
    },
    "sensor2": {
        "max_invalid_ration": 0.2,
    },
    "sensor3": {
        "max_invalid_ration": 0.0,
    },
    "sensor4": {
        "max_invalid_ration": 0.3,
    },
}

