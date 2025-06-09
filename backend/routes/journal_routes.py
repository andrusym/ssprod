from flask import Blueprint
journal_routes = Blueprint('journal_routes', __name__)

@journal_routes.route('/journal/entries')
def journal_entries():
    return {"entries": ["Trade 1", "Trade 2", "Trade 3"]}
