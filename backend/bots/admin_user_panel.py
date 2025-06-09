def render_admin_dashboard():
        """ Generates a status report for the admin dashboard with system metrics. """
    return {
        "status": "ok",
        "metrics": {
            "active_users": 12,
            "queued_orders": 5,
            "last_restart": "2025-06-01 10:32"
        }
    }