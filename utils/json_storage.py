import json
import os
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, cls=DateTimeEncoder, indent=4)

def load_from_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    return None
