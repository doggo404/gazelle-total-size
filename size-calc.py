import requests
import json
import hurry.filesize

endpoint = 'example.com'
cookie = 'session='
headers = {'cookie': cookie}
count = 1
size = 0
while count < 35000: #change the numer to the id of the newest upload
    count = count + 1
    info_url = f'https://{endpoint}/ajax.php?action=torrent&id=' + str(count)
    torrent_status = requests.get(info_url, headers=headers)
    torrent_info = json.loads(torrent_status.content)
    status = torrent_info['status']
    if status == 'success':
            size_bytes = torrent_info['response']['torrent']['size']
            size = size + size_bytes
            torrent_size = hurry.filesize.size(size)
            print(f'Total size up to https://{endpoint}/torrents.php?torrentid={count}  :  {torrent_size} , {size}B')
