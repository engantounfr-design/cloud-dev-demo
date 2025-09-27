from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 8000

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Server running at http://{host}:{port}")
server.serve_forever()
