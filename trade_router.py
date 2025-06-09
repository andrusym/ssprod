from flask import Blueprint
router = Blueprint('trade_router', __name__)

@router.route('/trade/status')
def trade_status():
    return {"status": "connected", "open_trades": 2}