from collections import defaultdict
from typing import Dict, List

def compute_metrics(parsed_data: dict) -> Dict:
    """
    
    :return: Description
    :rtype: Dict
    """
    total_sensors = len(parsed_data)
    total_invalid = 0
    total_valid = 0
    sensors_with_errors = []
    
    for sensor, data in parsed_data.items():
        valid_count = len(data["valid"])
        invalid_count = len(data["invalid"])

        total_valid += valid_count
        total_invalid += invalid_count

        if invalid_count > 0:
            sensors_with_errors.append(sensor)

    total_readings = total_valid + total_invalid
    invalid_ratio = (
        total_invalid / total_readings if total_readings > 0 else 0
    )

    metrics = {
        "total_sensors": total_sensors,
        "total_readings": total_readings,
        "valid_readings": total_valid,
        "invalid_readings": total_invalid,
        "invalid_ratio": round(invalid_ratio, 3),
        "sensors_with_errors": sensors_with_errors,
    }

    return metrics