import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

#sajat hely
BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#nircmd keresese
NIRCMD = os.path.join(BASE_DIR, "nircmd.exe")
#hangero
def hangfel():
    os.system(f'"{NIRCMD}" changesysvolume 5000')
def hangle():
    os.system(f'"{NIRCMD}" changesysvolume -5000')
def mute_unmute():
    os.system(f'"{NIRCMD}" mutesysvolume 2')
#lejatszas megallitas stb

#HTTP jelfogadas
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"utvonal: {self.path}")  

        #favico az mindegy
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        #funkcio valasztas
        if self.path == "/pause":
            try: 
                print("Play/Pause a bejovo")
                
            except:
                print("valami nem jo a playpause callba")
        elif self.path == "/hangfel":
            try: 
                print("hangfel a bejovo")
                hangfel()
            except:
                print("valami nem jo a hangfel callba")
        elif self.path == "/hangle":
            try: 
                print("hangle a bejovo")
                hangle()
            except:
                print("valami nem jo a hangle callba")
        elif self.path == "/mute":
            try: 
                print("mute a bejovo")
                mute_unmute()
            except:
                print("valami nem jo a mute callba")
        message = f"bejovo: {self.path}"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", str(len(message)))
        self.end_headers()
        self.wfile.write(message.encode())

#szerver inditasa
def szerverindit():
    try:
        server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
        print("HTTP szerver megy port 8000-en")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nSzerver leall.")
#main cuccok
if __name__ == "__main__":
    szerverindit()