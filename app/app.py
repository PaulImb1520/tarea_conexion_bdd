from flask import Flask, jsonify, request
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


@app.route("/users", methods=["GET"])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    email = new_user.get("email")
    
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (%s, %s)", (username, email)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User added successfully"}), 201



if __name__ == "__main__":
    app.run(host="0.0.0.0")
