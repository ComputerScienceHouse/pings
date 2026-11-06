"""
    csh-pings-backend.py - The main file for the CSH Pings Backend.
    Copyright (C) 2026 R. Mamet <flower@csh.rit.edu>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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

def main():
    httpd = HTTPServer(('localhost',5500),Serv)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
