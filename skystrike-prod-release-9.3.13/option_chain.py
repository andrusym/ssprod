import requests
import os

TRADIER_BASE_URL = "https://sandbox.tradier.com/v1"
TRADIER_TOKEN = os.getenv("TRADIER_API_KEY")

from utils.pricing import get_option_chain
    url = f"{TRADIER_BASE_URL}/markets/options/chains"
    headers = {
        "Authorization": f"Bearer {TRADIER_TOKEN}",
        "Accept": "application/json"
    }
    params = {
        "symbol": ticker,
        "expiration": expiry_date,
        "greeks": "false"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    calls = {}
    puts = {}
    if "options" in data and "option" in data["options"]:
        for option in data["options"]["option"]:
            strike = float(option["strike"])
            if option["option_type"] == "call":
                calls[strike] = {"bid": option["bid"], "ask": option["ask"]}
            elif option["option_type"] == "put":
                puts[strike] = {"bid": option["bid"], "ask": option["ask"]}
    return {"calls": calls, "puts": puts}