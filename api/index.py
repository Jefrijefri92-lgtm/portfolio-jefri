from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        file_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'index.html')
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        self.wfile.write(html.encode())
        return
