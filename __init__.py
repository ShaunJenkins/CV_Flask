from flask import Flask,render_template
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__) #creating flask app name
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

@app.route('/consultation/5625719273')
def view_messages():
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('consultation.db')
        cursor = conn.cursor()
        
        # Retrieve messages from the database
        cursor.execute('SELECT * FROM messages')
        messages = cursor.fetchall()
        
        # Close the database connection
        conn.close()
        
        # Render template with messages
        return render_template('consultation.html', messages=messages)
    except Exception as e:
        return str(e)


@app.route('/')
def home():
    return render_template("resume_2.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_1.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")


if(__name__ == "__main__"):
    app.run()
