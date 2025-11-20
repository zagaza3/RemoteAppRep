import os
import sys
import pyautogui
from http.server import BaseHTTPRequestHandler, HTTPServer

#sajat hely
BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#nircmd keresese
NIRCMD = os.path.join(BASE_DIR, "nircmd.exe")
#pause exe ahk keresese
PAUSE_EXE = os.path.join(BASE_DIR, "pause.exe")
#hangero
def hangfel():
    os.system(f'"{NIRCMD}" changesysvolume 5000')
def hangle():
    os.system(f'"{NIRCMD}" changesysvolume -5000')
def mute_unmute():
    os.system(f'"{NIRCMD}" mutesysvolume 2')
#lejatszas megallitas elore hatra tekeres stb
def megallit_indit():
    os.system(f'"{PAUSE_EXE}"')
def elore():
    pyautogui.press('right')
def hatra():
    pyautogui.press('left')
#pc iranyitas alapfunkciok
def leallitas():
    os.system('shutdown /s /t 0')
#eger mozgatas, egergomb, scroll
def egermozgatfel():
    x, y = pyautogui.position()
    pyautogui.moveTo(x, y - 20)
def egermozgatle():
    x, y = pyautogui.position()
    pyautogui.moveTo(x, y + 20)
def egermozgatbal():
    x, y = pyautogui.position()
    pyautogui.moveTo(x - 20, y)
def egermozgatjobb():
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 20, y)
def egerBal():
    pyautogui.click()
def egerJobb():
    pyautogui.click(button='right')
def felgorget():
    pyautogui.scroll(100)
def legorget():
    pyautogui.scroll(-100)
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
                megallit_indit()
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
        elif self.path == "/inditallit":
            try: 
                print("inditallit a bejovo")
                megallit_indit()
            except:
                print("valami nem jo a inditallit callba")
        elif self.path == "/leallit":
            try: 
                print("leallit a bejovo")
                leallitas()
            except:
                print("valami nem jo a leallit callba")
        elif self.path == "/egerfel":
            try: 
                print("egerfel a bejovo")
                egermozgatfel()
            except:
                print("valami nem jo a egerfel callba")
        elif self.path == "/egerle":
            try: 
                print("egerle a bejovo")
                egermozgatle()
            except:
                print("valami nem jo a egerle callba")
        elif self.path == "/egerbal":
            try: 
                print("egerbal a bejovo")
                egermozgatbal()
            except:
                print("valami nem jo a egerbal callba")
        elif self.path == "/egerjobb":
            try: 
                print("egerjobb a bejovo")
                egermozgatjobb()
            except:
                print("valami nem jo a egerjobb callba")
        elif self.path == "/balclick":
            try: 
                print("balclick a bejovo")
                egerBal()
            except:
                print("valami nem jo a balclick callba")
        elif self.path == "/jobbclick":
            try: 
                print("jobbclick a bejovo")
                egerJobb()
            except:
                print("valami nem jo a jobbclick callba")
        elif self.path == "/fel":
            try: 
                print("fel a bejovo")
                felgorget()
            except:
                print("valami nem jo a fel callba")
        elif self.path == "/le":
            try: 
                print("le a bejovo")
                legorget()
            except:
                print("valami nem jo a le callba")
        elif self.path == "/elore":
            try: 
                print("elore a bejovo")
                elore()
            except:
                print("valami nem jo a elore callba")
        elif self.path == "/hatra":
            try: 
                print("hatra a bejovo")
                hatra()
            except:
                print("valami nem jo a hatra callba")
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