import requests
import re
import json
import html
import hurry.filesize
'''------------------------------- Input username and password below. ----------------------------'''



username = ""
password = ""



'''-----------------------------------------------------------------------------------------------'''
url = "https://test.link"
loginpage = str(url + "/login.php")

data = {"username": username,
        "password": password}

# Get auth token from request headers
r = requests.post(loginpage, data=data)
accountinfo = str(r.request.headers)
x = re.search(".*\s(session=.*)'}", accountinfo)
token = x.group(1)
headers = {'cookie': token}
count = 1
size = 0
while count < 35000: #change the numer to the id of the newest upload
    count = count + 1
    info_url = f'{url}/ajax.php?action=torrent&id=' + str(count)
    torrent_status = requests.get(info_url, headers=headers)
    torrent_info = json.loads(torrent_status.content)
    status = torrent_info['status']
    if status == 'success':
            size_bytes = torrent_info['response']['torrent']['size']
            size = size + size_bytes
            torrent_size = hurry.filesize.size(size)
            print(f'Cheching {url}/torrents.php?torrentid={count}  : Total size(Gb, Tb): {torrent_size} , {size}B')
