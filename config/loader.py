from pathlib import Path

import yaml


CONFIG_DIR = Path(__file__).parent


class Config:
    def __init__(self, environment: str):
        config_path = CONFIG_DIR / f"{environment}.yml"
        with config_path.open(encoding="utf-8") as config_file:
            values = yaml.safe_load(config_file)

        self.environment = values["environment"]
        self.web_base_url = values["web"]["base_url"]
        self.todo_base_url = values["web"]["todo_base_url"]
        self.playwright_base_url = values["web"]["playwright_base_url"]
        self.api_base_url = values["api"]["base_url"]
        self.default_timeout = values["timeouts"]["default"]
        self.navigation_timeout = values["timeouts"]["navigation"]
