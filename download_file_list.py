#!/usr/bin/python3

# download_file_list.py
# Download a list of files "links.txt" to ./downloads/[filename] (./downloads dir needs to exist)
# links.txt contains the full URL to the file(s)

import os.path
import urllib.request

links = open('links.txt', 'r')
for link in links:
        link = link.strip()
        filename = link.rsplit('/', 1)[-1]
        #filename = os.path.join('downloads', name)

        if not os.path.isfile(link):
                print('Downloading: ' + filename)
                local_file = './downloads/' + filename
                try:
                        urllib.request.urlretrieve(link, local_file)
                except Exception as inst:
                        print(inst)
                        print('  Encountered unknown error. Continuing.')
