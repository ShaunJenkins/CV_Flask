import sqlite3

def create_database():
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('consultation.db')
        cursor = conn.cursor()
        
        # Create messages table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                        (id INTEGER PRIMARY KEY, name TEXT, message TEXT)''')
        
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()
        print("Database created successfully.")
    except Exception as e:
        print("Error creating database:", e)

if __name__ == "__main__":
    create_database()
