from http.server import *
import volumeController
from volumeController import SetASessionsVolume
import json
import os

PORT = 8080
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        path = self.path
        if path == '/':
            filename = 'index.html'
        else:
            filename = path.lstrip('/')

        if os.path.exists(filename):
            self.send_response(200)

            if filename.endswith('.html'):
                self.send_header('Content-type', 'text/html')
            elif filename.endswith('.css'):
                self.send_header('Content-type', 'text/css')
            elif filename.endswith('.js'):
                self.send_header('Content-type', 'text/javascript')

            self.end_headers()

            with open(filename, 'rb') as fh:
                self.wfile.write(fh.read())
        else:
            self.send_response(404,"File Not Found!")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        for session in data:
            print(f"Session: {session['name']} | Volume: {session['volume']}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write("Data Sent")

    def do_HEAD(self):
        pass

    def do_PUT(self):
        pass


if __name__ == '__main__':
    server = HTTPServer(('', PORT), RequestHandler)
    print('Server started http://localhost:8080')
    server.serve_forever()
