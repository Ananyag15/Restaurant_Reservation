from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            date TEXT,
            time TEXT,
            guests INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reserve", methods=["POST"])
def reserve():
    name = request.form["name"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    guests = request.form["guests"]

    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservations (name, phone, date, time, guests)
        VALUES (?, ?, ?, ?, ?)
    """, (name, phone, date, time, guests))
    conn.commit()
    conn.close()

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
