from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

class LogShipperHandler(BaseHTTPRequestHandler):
    log_dir = '/var/log/pods'

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        for filepath in Path(self.log_dir).iterdir():
            if filepath.is_file():
                with filepath.open('r') as f:
                    self.wfile.write(f.read().encode())


def run(server_class=HTTPServer, handler_class=LogShipperHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
