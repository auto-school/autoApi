import json

def tojson(data):
    json_data = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)
    return json_data

def todict(raw_projects):
    return None