from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/', methods=['GET'])
def home():
    """Root endpoint that returns a welcome message.

    Returns:
        str: Welcome message.
    """
    data = "Welcome to the Flask API!"
    return data


@app.route('/data', methods=['GET'])
def data():
    """Endpoint that returns a list of all usernames stored in memory.

    Returns:
        Response: JSON array of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def status():
    """Endpoint to check the API status.

    Returns:
        str: The string "OK".
    """
    return jsonify("OK")


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Retrieve a specific user's data by username.

    Args:
        username (str): The username to search for.

    Returns:
        Response: JSON object with user data if found,
                  or error message if not found.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user via POST request.

    Request JSON format:
        {
            "username": "jane",
            "name": "Jane",
            "age": 28,
            "city": "Los Angeles"
        }

    Returns:
        Response: JSON message with new user data and status code 201
                  if successful, or error message and status code 400
                  if "username" field is missing.
    """
    new_user = request.get_json()
    if "username" in new_user:
        user = new_user["username"]
        users[user] = new_user
        print(user)
        return jsonify({"message": "User added", "user": new_user}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
