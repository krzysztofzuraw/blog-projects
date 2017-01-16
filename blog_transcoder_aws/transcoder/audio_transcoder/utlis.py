import json


def convert_sns_str_to_json(obj):
    value = obj.get('Message')
    if value and isinstance(value, str):
        obj['Message'] = json.loads(value)
    return obj
