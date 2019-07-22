import json


def is_json(json_data):
    try:
        json.loads(json_data)
        return True
    except ValueError:
        return False
