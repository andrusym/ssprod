from flask import Blueprint
setup_routes = Blueprint('setup_routes', __name__)

@setup_routes.route('/setup/init')
def setup_init():
    return {"setup": "complete", "timestamp": "2025-06-09"}
