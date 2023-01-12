from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("got a request")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response_string = (
            "<html><body>"
            "<h1>Hello client!</h1>"
            "</body></html>"
        )

        self.wfile.write(response_string.encode())



if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 1234), RequestHandler)
    server.serve_forever()