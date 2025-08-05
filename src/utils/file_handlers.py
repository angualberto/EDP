def read_json_file(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml_file(file_path):
    import yaml
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml_file(file_path, data):
    import yaml
    with open(file_path, 'w') as file:
        yaml.dump(data, file)