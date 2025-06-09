
# pair_trading_engine.py

import logging
from utils.market_data import get_price_series
from utils.broker_api import execute_trade

class PairTradingEngine:
    def __init__(self, ticker_1, ticker_2, lookback_days=30):
        self.ticker_1 = ticker_1
        self.ticker_2 = ticker_2
        self.lookback = lookback_days

    def analyze_and_trade(self):
        prices_1 = get_price_series(self.ticker_1, self.lookback)
        prices_2 = get_price_series(self.ticker_2, self.lookback)

        if not prices_1 or not prices_2:
            logging.warning("[PairTradingEngine] Insufficient data")
            return None

        spread = [p1 - p2 for p1, p2 in zip(prices_1, prices_2)]
        mean_spread = sum(spread) / len(spread)
        current_spread = prices_1[-1] - prices_2[-1]

        logging.info(f"[PairTradingEngine] Spread: {current_spread:.2f}, Mean: {mean_spread:.2f}")

        if current_spread > mean_spread * 1.5:
            # Mean reversion setup
            return execute_trade({
                "type": "pair_trade",
                "entry": "short_spread",
                "ticker_1": self.ticker_1,
                "ticker_2": self.ticker_2
            })
        elif current_spread < mean_spread * 0.5:
            return execute_trade({
                "type": "pair_trade",
                "entry": "long_spread",
                "ticker_1": self.ticker_1,
                "ticker_2": self.ticker_2
            })
        else:
            logging.info("[PairTradingEngine] No trade signal")
            return None
