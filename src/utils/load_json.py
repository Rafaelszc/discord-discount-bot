import json

def load_json(json_path: str) -> json.load:
    js = open(json_path)
    data_json = json.load(js)

    return data_json