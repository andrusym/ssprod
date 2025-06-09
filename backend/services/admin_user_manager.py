def get_all_users():
        """ Returns a list of all users in the system for admin purposes. """
    return [{"username": "admin", "role": "superuser"}]

def add_user(username, role="user"):
        """ Adds a new user to the system with a specified role. """
    return {"username": username, "role": role, "status": "added"}