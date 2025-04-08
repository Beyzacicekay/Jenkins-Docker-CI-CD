import http.server
import socketserver

PORT = 80

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Sunucu port başlatıldııı: http://localhost:80")
    httpd.serve_forever()
