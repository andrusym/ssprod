
import logging

def execute_order(order_data):
    logging.info(f"Executing order: {order_data}")
    # Simulate order placement
    result = place_order(order_data)
    log_trade(result)
    return {"status": "success", "details": result}

def place_order(order_data):
    return {"symbol": order_data.get("symbol"), "action": order_data.get("action"), "qty": order_data.get("quantity")}

def log_trade(trade):
    logging.info(f"Trade logged: {trade}")
