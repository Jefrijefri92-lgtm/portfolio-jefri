from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = '<h1>UDAH BISA JEFRI!</h1><p>Typo ginocorn kelar. 5 jam 10 menit tamat.</p>'
        self.wfile.write(html.encode())
        return
