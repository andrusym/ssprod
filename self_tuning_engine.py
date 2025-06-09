
# self_tuning_engine.py

import logging
from utils.database import get_strategy_metrics, update_bot_params

class SelfTuningEngine:
    def __init__(self, strategies):
        self.strategies = strategies

    def tune_all(self):
        for bot in self.strategies:
            metrics = get_strategy_metrics(bot)
            new_params = self._adjust_params(metrics)
            update_bot_params(bot, new_params)
            logging.info(f"[SelfTuningEngine] Updated {bot} parameters: {new_params}")

    def _adjust_params(self, metrics):
        scale_factor = 1.0
        if metrics['win_rate'] > 0.65:
            scale_factor += 0.2
        elif metrics['drawdown'] < -0.1:
            scale_factor -= 0.3
        return {"contract_multiplier": round(scale_factor, 2)}
