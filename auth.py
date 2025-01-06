import json
import os

def load_users():
    # Check if the users.json file exists and has content
    if os.path.exists('users.json') and os.path.getsize('users.json') > 0:
        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in users.json.")
            users = []
    else:
        users = []
    return users

# Save users to a JSON file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)  # Add indent for better readability

# Authenticate user (now returns user data)
def authenticate(email, password):
    users = load_users()
    for user in users:
        if user['email'] == email and user['password'] == password:
            return user  # Return the user data (including username)
    return None  # Return None if authentication fails

# Register user (Sign Up)
def register(username, password, email):
    users = load_users()

    # Check if the email already exists (since emails should be unique)
    for user in users:
        if user['email'] == email:
            return False  # Email already exists, so registration fails
    
    # If the email doesn't exist, create a new user with the username
    users.append({'username': username, 'password': password, 'email': email})
    save_users(users)
    return True
