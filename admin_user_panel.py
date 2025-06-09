import streamlit as st
from admin_user_manager import load_users, add_user, delete_user, update_user

st.title("Admin User Management")

users = load_users()
st.write("Current Users:", users)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
tradier_token = st.text_input("Tradier Token")

if st.button("Add User"):
    try:
        add_user(username, password, tradier_token)
        st.success("User added successfully.")
    except ValueError as e:
        st.error(str(e))

if st.button("Update User"):
    update_user(username, password, tradier_token)
    st.success("User updated.")

if st.button("Delete User"):
    delete_user(username)
    st.success("User deleted.")