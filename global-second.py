from ipytv import playlist
from ipytv.playlist import M3UPlaylist
from ipytv.channel import IPTVChannel

url = "http://tv.multitv.live:25461/get.php?username=Martha11CA&password=I4bSzJfAzE&type=m3u_plus"
pl = playlist.loadu(url)
groupTitleAccepted = [
    'SERIES-ESTRENOS',
    'SERIES-DRAMA',
    'SERIES-CRIMEN',
    'SERIES-DOCUMENTALES',
    'SERIES-CIENCIA FICCION',
    'SERIES-WESTERN',
    'SERIES-REALITY',
    'SERIES-COMEDIA',
    'SERIES-NOVELA',
    'SERIES-ACCION',
    'VOD-ESTRENO',
    'VOD-HORROR',
    'VOD-DOCUMENTALES',
    'VOD-BELICAS',
    'VOD-ACCION',
    'VOD-DRAMA'
]

plGlobal2 = M3UPlaylist()

with open('global2.m3u', 'w', encoding='utf-8') as out_file:
    
    for channel in pl:
        if (any(substring in channel.attributes["group-title"] for substring in groupTitleAccepted)):
            plGlobal2.append_channel(channel)
            print(f'group: {channel.attributes["group-title"]} channel \"{channel.name}\": {channel.url}')

    out_file.write(plGlobal2.to_m3u_plus_playlist())