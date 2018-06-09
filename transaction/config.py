import json
import os

CONFIG_FILE = os.environ.get("CONFIG_FILE", "config.json")

try: 
    with open(CONFIG_FILE, 'r') as json_data_file:
        cfg = json.load(json_data_file)
except FileNotFoundError:
    print("Could not find config file '{}'".format(CONFIG_FILE))
    cfg = {}

for key in ["DB_USERNAME", "DB_PASSWORD", "DB_HOST_URL"]:
    if key not in cfg:
        cfg[key] = None
    cfg[key] = os.environ.get(key, cfg[key])
