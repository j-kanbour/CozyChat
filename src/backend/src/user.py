from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple in-memory user database (replace with a real database in production)
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    print(username, password)
    # if not username or not password:
    #     return jsonify({"message": "Username and password are required"}), 400

    # user = next((user for user in users if user["username"] == username), None)
    # if user is None or user["password"] != password:
    #     return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(debug=True)
