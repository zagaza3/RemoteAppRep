import os
from http.server import BaseHTTPRequestHandler, HTTPServer
#hangero
def hangfel():
    os.system('powershell -command "$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys([char]175)"')
def hangle():
    os.system('powershell -command "$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys([char]174)"')
def mute():
    os.system('powershell -command "$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys([char]173)"')
#lejatszas megallitas stb
def plpause():
    os.system('powershell -command "$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys([char]179)"')
def elozo():
    os.system('powershell -command "$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys([char]177)"')
def kovetkezo():
    os.system('powershell -command "$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys([char]176)"')
#HTTP jelfogadas
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"utvonal: {self.path}")  # prints to terminal

        # Respond to browser
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