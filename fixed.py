import random
import sqlite3
import os
import secrets


# Issue 1: Hardcoded credentials
DB_PASSWORD = os.environ.get('DB_PASSWORD')
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
# Issue 2: SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()
def generate_token():
# Issue 3: Insecure random number for security token
    return str(secrets.randbelow(900000) + 100000)
# Issue 4: Unused variable

print(get_user('admin'))
print(generate_token())