import http.server
import time
from ipytv import playlist
from ipytv.playlist import M3UPlaylist
from ipytv.channel import IPTVChannel

PORT = 80

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url = "http://tv.dominiotv.xyz:25461/get.php?username=Rolando&password=Rolando2021&type=m3u_plus"
        pl = playlist.loadu(url)

        plGlobal = M3UPlaylist()

        for channel in pl:
            channel.attributes["tvg-id"] = channel.attributes["tvg-name"]
            plGlobal.append_channel(channel)

        self.send_response(200)
        self.send_header("Content-Type", "text/txt")
        self.end_headers()
        self.wfile.write(plGlobal.to_m3u_plus_playlist().encode())

if __name__ == '__main__':
    serverAddress = ('', PORT)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()