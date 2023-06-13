import http.server
import time
import threading
from ipytv import playlist
from ipytv.playlist import M3UPlaylist
from ipytv.channel import IPTVChannel

PORT = 8000

def download_m3u():
    print("Downloading m3u playlist...\n")
    url = "http://tv.dominiotv.xyz:25461/get.php?username=Rolando&password=Rolando2021&type=m3u_plus"
    global pl
    pl = playlist.loadu(url)

    for channel in pl:
        if (channel.attributes["tvg-id"] == ""):
            channel.attributes["tvg-id"] = channel.attributes["tvg-name"]
    
    threading.Timer(300.0, download_m3u).start()

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/txt")
        self.end_headers()
        self.wfile.write(pl.to_m3u_plus_playlist().encode())

if __name__ == '__main__':
    download_m3u()
    print("Stating server...\n")
    serverAddress = ('', PORT)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()