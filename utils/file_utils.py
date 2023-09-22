import os
import yaml

def read_yaml(file_path, default_config):
    if not os.path.exists(file_path):
        write_yaml(file_path, default_config)
        return default_config

    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def write_yaml(file_path, config):
    with open(file_path, 'w') as f:
        yaml.safe_dump(config, f)
