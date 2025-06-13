#!/usr/bin/python3
"""
Flask API example with HTTP Basic Auth and JWT authentication.

Provides endpoints protected by HTTP Basic Authentication and JWT tokens.
Supports role-based access control for admin-only routes.

Endpoints:
    /basic-protected  (GET)   - Requires HTTP Basic Auth
    /login            (POST)  - Authenticate user and receive JWT token
    /jwt-protected    (GET)   - Requires valid JWT token
    /admin-only       (GET)   - Requires JWT token with admin role

JWT error handlers provide meaningful JSON error messages on token issues.

Modules used:
    flask
    flask_httpauth
    werkzeug.security
    flask_jwt_extended

Users are hardcoded with password hashes and roles for demo purposes.
"""
from flask import Flask
from flask import request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

app = Flask(__name__)

auth = HTTPBasicAuth()

app.config["SECRET_KEY"] = "SuPeR-SeCrEt74"

jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for HTTP Basic Auth.

    Args:
        username (str): Username provided by client.
        password (str): Password provided by client.

    Returns:
        str or None: Username if valid credentials, else None.
    """
    user = users.get(username)
    if (
        user and
        check_password_hash(user['password'], password)
    ):
        return username
    return None


@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized access"}), 401


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Basic Auth protected endpoint.

    Returns:
        JSON message confirming access granted.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and provide JWT access token.

    Expects JSON body with 'username' and 'password'.

    Returns:
        JSON with access_token if credentials valid,
        or JSON error with 401 status otherwise.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)
    if username not in users or not (
        check_password_hash(user["password"], password)
    ):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity={'username': username,
                                                 'role': user['role']})
    return jsonify(access_token=access_token)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """JWT protected endpoint.

    Requires valid JWT token.

    Returns:
        JSON message confirming JWT access granted.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Admin-only endpoint.

    Requires valid JWT token and user role 'admin'.

    Returns:
        JSON message confirming admin access,
        or JSON error with 403 status if not admin.
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handler for missing or unauthorized JWT token.

    Returns:
        JSON error message with 401 status.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handler for invalid JWT token.

    Returns:
        JSON error message with 401 status.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handler for expired JWT token.

    Returns:
        JSON error message with 401 status.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handler for revoked JWT token.

    Returns:
        JSON error message with 401 status.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handler for fresh JWT token required.

    Returns:
        JSON error message with 401 status.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
