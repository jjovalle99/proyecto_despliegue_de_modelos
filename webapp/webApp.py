import http.server
import socketserver
from flask import Flask, render_template

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor web en el puerto", PORT)
    httpd.serve_forever()

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)
