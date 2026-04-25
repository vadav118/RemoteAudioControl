from http.server import *
import volumeController
from volumeController import SetASessionsVolume
import json
PORT = 8080
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        filename = "index.html"
        fh = open(filename, "rb")
        self.send_response(200)
        self.send_header("Content-type", "html")
        self.end_headers()


        string = fh.read()
        self.wfile.write(string)

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
