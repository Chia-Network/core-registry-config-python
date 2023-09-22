# python-template
Template repo for Python-based projects

```python
from core_registry_config import ConfigManager

# Define default config
default_config = {
    "TOKENIZATION_ENGINE": {
        "DATA_LAYER_HOST": "https://localhost:8562",
        "WALLET_HOST": "https://localhost:9256",
        "LOG_LEVEL": "info",
        "BIND_ADDRESS": "localhost"
    }
}

# Initialize the ConfigManager
config_manager = ConfigManager(default_config=default_config)

# Fetch the entire configuration
current_config = config_manager.get_config()
print("Current Config:", current_config)

# Update a specific key-value pair in the configuration
update_data = {
    "TOKENIZATION_ENGINE": {
        "DATA_LAYER_HOST": "https://newhost:8562"
    }
}
config_manager.update_config(update_data)

# Fetch the updated configuration
updated_config = config_manager.get_config()
print("Updated Config:", updated_config)

```