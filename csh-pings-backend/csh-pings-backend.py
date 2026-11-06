from http.server import HTTPServer, BaseHTTPRequestHandler

# TODO: Add CSH Auth
AUTHENTICATED = True
USERNAME = "@username"

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/status':
            file_to_open = "You are connected :3"
            self.send_response(200)
        elif (self.path == "/api/status") and AUTHENTICATED:
            file_to_open = f"Welcome {USERNAME}! You are connected :3"
            self.send_response(200)
        else:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost',5500),Serv)
httpd.serve_forever()

