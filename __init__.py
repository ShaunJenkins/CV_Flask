from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_database_connection():
    return sqlite3.connect('consultation.db')

@app.route('/consultation/5625719273')
def view_messages():
    try:
        # Connect to SQLite database
        conn = get_database_connection()
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

@app.route('/create_message', methods=['POST'])
def create_message():
    try:
        data = request.json
        name = data['name']
        message = data['message']
        
        # Connect to SQLite database
        conn = get_database_connection()
        cursor = conn.cursor()
        
        # Insert data into the database
        cursor.execute('INSERT INTO messages (name, message) VALUES (?, ?)', (name, message))
        
        # Commit the transaction and close the connection
        conn.commit()
        conn.close()
        
        return jsonify({"message": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


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
