from http.server import *
import volumeController
from volumeController import SetASessionsVolume


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        filename = "index.html"
        fh = open(filename, "rb")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


        string = fh.read()
        self.wfile.write(string)

    def do_POST(self):
        pass

    def do_HEAD(self):
        pass

    def do_PUT(self):
        pass


if __name__ == '__main__':
    server = HTTPServer(('', 8080), RequestHandler)
    print('Server started http://localhost:8080')
    server.serve_forever()
