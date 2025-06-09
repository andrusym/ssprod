import json
import os

USERS_FILE = "data/users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def add_user(username, password, tradier_token):
    users = load_users()
    if any(u["username"] == username for u in users):
        raise ValueError("User already exists.")
    users.append({"username": username, "password": password, "tradier_token": tradier_token})
    save_users(users)

def get_user(username):
    users = load_users()
    return next((u for u in users if u["username"] == username), None)

def update_user(username, password=None, tradier_token=None):
    users = load_users()
    for user in users:
        if user["username"] == username:
            if password:
                user["password"] = password
            if tradier_token:
                user["tradier_token"] = tradier_token
    save_users(users)

def delete_user(username):
    users = load_users()
    users = [u for u in users if u["username"] != username]
    save_users(users)