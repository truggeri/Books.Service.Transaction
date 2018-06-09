import json
import os

CONFIG_FILE = os.environ.get("CONFIG_FILE", "config.json")

with open(CONFIG_FILE) as json_data_file:
    cfg = json.load(json_data_file)

for key in ["DB_USERNAME", "DB_PASSWORD", "DB_HOST_URL"]:
    if not key in cfg:
        cfg[key] = None
    cfg[key] = os.environ.get(key, cfg[key])
