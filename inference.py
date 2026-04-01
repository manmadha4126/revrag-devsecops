from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

    def do_POST(self):
        if self.path == "/reset":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "reset successful"}).encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
server.serve_forever()