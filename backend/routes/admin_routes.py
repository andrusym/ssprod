from flask import Blueprint
admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin/panel')
def admin_panel():
    return {"status": "Admin panel OK"}
