from option_chain import get_option_chain
from utils.pricing import calculate_iron_condor_price
from ml_engine import score_strategy

class IronCondorStrategy:
    def __init__(self, ticker, expiry_date, capital, config):
        self.ticker = ticker
        self.expiry_date = expiry_date
        self.capital = capital
        self.config = config

    def find_condor_setup(self):
from utils.pricing import get_option_chain
        strikes = sorted(chain["calls"].keys())
        if len(strikes) < 4:
            raise ValueError("Not enough strikes to construct Iron Condor.")

        mid = len(strikes) // 2
        short_put = strikes[mid - 2]
        long_put = strikes[mid - 3]
        short_call = strikes[mid + 2]
        long_call = strikes[mid + 3]

        setup = {
            "short_put": short_put,
            "long_put": long_put,
            "short_call": short_call,
            "long_call": long_call,
            "expiry": self.expiry_date,
            "option_chain": chain
        }
        return setup

    def enter_trade(self):
        setup = self.find_condor_setup()
        entry_price = calculate_iron_condor_price(
            self.ticker,
            setup["expiry"],
            setup["long_put"],
            setup["short_put"],
            setup["short_call"],
            setup["long_call"],
            setup["option_chain"]
        )
        ml_score = score_strategy("IronCondor", self.ticker, setup)
        contracts = int(self.capital / (entry_price * 100))
        return {
            "ticker": self.ticker,
            "type": "IronCondor",
            "legs": setup,
            "entry_price": entry_price,
            "contracts": contracts,
            "capital_used": round(contracts * entry_price * 100, 2),
            "ml_score": ml_score
        }