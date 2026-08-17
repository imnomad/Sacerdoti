import http.server
import socketserver
import threading
import urllib.request
import time
import os

PORT = 8089
DIRECTORY = os.getcwd()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('', PORT), CustomHandler)
thread = threading.Thread(target=httpd.serve_forever, daemon=True)
thread.start()

time.sleep(0.5)

urls = [
    'http://localhost:8089/index.html',
    'http://localhost:8089/historia.html',
    'http://localhost:8089/procesos.html',
    'http://localhost:8089/productos.html',
    'http://localhost:8089/estuches.html',
    'http://localhost:8089/estuchespromocionales.html',
    'http://localhost:8089/materialpop.html',
    'http://localhost:8089/promocion.html',
    'http://localhost:8089/clientes.html',
    'http://localhost:8089/contacto.html',
    'http://localhost:8089/css/main.css',
    'http://localhost:8089/js/app.js',
    'http://localhost:8089/assets/logos/logochico.png'
]

success = 0
for u in urls:
    try:
        resp = urllib.request.urlopen(u, timeout=3)
        if resp.status == 200:
            content = resp.read()
            success += 1
            print(f'OK: {u} (size: {len(content)} bytes)')
    except Exception as e:
        print(f'ERROR on {u}: {e}')

print(f'\n--- TEST SUMMARY ---')
print(f'Tested {len(urls)} assets: {success}/{len(urls)} loaded successfully with HTTP 200.')
httpd.shutdown()
