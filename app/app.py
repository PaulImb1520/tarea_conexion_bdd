from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host="db",  # El nombre del servicio del contenedor de la base de datos
        user="myuser",
        password="mypassword",
        database="mydatabase",
    )
    return connection


@app.route("/users")
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
