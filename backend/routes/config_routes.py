from flask import Blueprint
config_routes = Blueprint('config_routes', __name__)

@config_routes.route('/config')
def config_page():
    return {"config": {"max_trades": 5, "env": "prod"}}
