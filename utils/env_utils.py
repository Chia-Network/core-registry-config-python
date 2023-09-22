import os

def update_config_with_env(config):
    for key, value in os.environ.items():
        keys = key.split('__')
        temp_config = config
        for k in keys[:-1]:
            temp_config = temp_config.get(k, {})
        if keys[-1] in temp_config:
            temp_config[keys[-1]] = value
    return config
