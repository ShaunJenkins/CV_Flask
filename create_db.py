from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create SQLite database connection
conn = sqlite3.connect('consultation.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                (id INTEGER PRIMARY KEY, name TEXT, message TEXT)''')

# Commit the transaction
conn.commit()

@app.route('/create_db.py', methods=['POST'])
def create_entry():
    data = request.json
    name = data['name']
    message = data['message']
    try:
        # Insert data into the database
        cursor.execute('INSERT INTO messages (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        return jsonify({"message": "success"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"message": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
