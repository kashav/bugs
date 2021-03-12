#!/usr/bin/env python3
#
# python3 server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>hello</h1></body></html>")


if __name__ == "__main__":
    HTTPServer(("localhost", 8000), Handler).serve_forever();

