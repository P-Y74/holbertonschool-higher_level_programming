#!/usr/bin/python3
"""
A simple HTTP server using Python's built-in http.server module.

This server handles basic GET requests on multiple endpoints:
- "/"      : returns a plain text welcome message.
- "/data"  : returns sample JSON data.
- "/status": returns a simple status message.
- "/info"  : returns API information in JSON format.
- Any other endpoint returns a 404 Not Found error.

Usage:
    Run this script and navigate to http://localhost:8000 in your browser
    or use curl to test the endpoints.

Example:
    curl http://localhost:8000/data
"""


from http.server import *
from urllib.parse import *
import json


class BasicServer(BaseHTTPRequestHandler):
    """
    HTTP request handler class to serve different endpoints.

    Methods
    -------
    do_GET():
        Handles GET requests for several endpoints and returns
        appropriate responses.

    Endpoints handled:
        "/"      : Plain text welcome message.
        "/data"  : JSON data with user information.
        "/status": Plain text "OK".
        "/info"  : JSON with API version and description.
        Others   : Responds with 404 Not Found.
    """

    def do_GET(self):
        """
        Handle GET HTTP requests.

        Parses the request path and serves content based on the endpoint.

        Returns:
            HTTP 200 responses with content for known endpoints.
            HTTP 404 response for unknown endpoints.
        """
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == "/":
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif path == "/data":
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif path == "/status":
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        elif path == "/info":
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")


port = HTTPServer(('', 8000), BasicServer)
try:
    port.serve_forever()
except KeyboardInterrupt:
    pass
