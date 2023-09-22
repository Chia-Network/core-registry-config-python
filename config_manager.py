from .utils.file_utils import read_yaml, write_yaml
from .utils.env_utils import update_config_with_env

class ConfigManager:
    def __init__(self, default_config, chia_root, persistence_folder="core-registry"):
        self.default_config = default_config
        self.chia_root = chia_root
        self.persistence_folder_path = f"{self.chia_root}/{persistence_folder}"
        self.config_file_path = f"{self.persistence_folder_path}/config.yaml"
        self.config = self._get_config()

    def _get_config(self):
        config = read_yaml(self.config_file_path, self.default_config)
        config = update_config_with_env(config)
        write_yaml(self.config_file_path, config)
        return config
