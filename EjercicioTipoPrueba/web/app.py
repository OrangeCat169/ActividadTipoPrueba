from flask import Flask
import mysql.connector
import time
import os

app = Flask(__name__)

# Esperar que MySQL esté listo
time.sleep(10)

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM personas")
    nombres = [row[0] for row in cursor.fetchall()]
    conn.close()

    return "<br>".join(nombres)


@app.route("/health")
def health():
    try:
        conn = get_connection()
        conn.close()
        return "OK", 200
    except:
        return "DB connection failed", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
