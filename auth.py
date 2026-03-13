import bcrypt
from database import get_connection

def register_user(username, password, role="viewer"):
    conn = get_connection()
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    query = "INSERT INTO users (username, password_hash, role) VALUES (%s,%s,%s)"
    cursor.execute(query, (username, password_hash.decode(), role))

    conn.commit()
    cursor.close()
    conn.close()

    print("User registered successfully")


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT password_hash, role FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        stored_hash, role = result

        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            print("Login successful")
            print("Role:", role)
            return True
        else:
            print("Incorrect password")
            return False
    else:
        print("User not found")
        return False
