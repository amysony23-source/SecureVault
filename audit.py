import hashlib
import json
import os
from datetime import datetime

LOG_FILE = "logs/audit_log.json"


def get_last_hash():
    if not os.path.exists(LOG_FILE):
        return "0"

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    if len(logs) == 0:
        return "0"

    return logs[-1]["hash"]


def create_hash(entry):
    data = f"{entry['timestamp']}{entry['user']}{entry['action']}{entry['ip']}{entry['prev_hash']}"
    return hashlib.sha256(data.encode()).hexdigest()


def log_action(user, action, ip="127.0.0.1"):
    log_entry = {
        "timestamp": str(datetime.now()),
        "user": user,
        "action": action,
        "ip": ip,
        "prev_hash": get_last_hash()
    }

    log_entry["hash"] = create_hash(log_entry)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    print("Audit log recorded.")
