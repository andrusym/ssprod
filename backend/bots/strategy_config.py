
# strategy_config.py

import logging
from utils.database import get_strategy_config, save_strategy_config

class StrategyConfigManager:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_config(self, strategy_name):
        config = get_strategy_config(self.user_id, strategy_name)
        if not config:
            logging.warning(f"[StrategyConfig] No config found for {strategy_name}")
        return config

    def update_config(self, strategy_name, config_updates):
        current = get_strategy_config(self.user_id, strategy_name) or {}
        updated = {**current, **config_updates}
        save_strategy_config(self.user_id, strategy_name, updated)
        logging.info(f"[StrategyConfig] Updated {strategy_name} config for user {self.user_id}")
        return updated
