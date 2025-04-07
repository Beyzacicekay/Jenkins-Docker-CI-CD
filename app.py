import http.server
import socketserver

PORT = 80

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Sunucu başlatıldı: http://localhost:80")
    httpd.serve_forever()
