import bcrypt
from database import connect_db, create_user_table

create_user_table()

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode('utf-8'))


def add_user(username, password, role):
    conn = connect_db()
    cursor = conn.cursor()

    hashed = hash_password(password).decode('utf-8')


    try:
        cursor.execute("INSERT INTO users(username, password, role) VALUES(?, ?, ?)",
                       (username, hashed, role))
        conn.commit()
        print(f"User '{username}' added successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT password, role FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash, role = result
        if check_password(password, stored_hash):
            print(f"Login successful! Role: {role}")
            return role
    print("Login failed: Invalid username or password")
    return None
