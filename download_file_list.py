#!/usr/bin/python3

# download_file_list.py
# Download a list of files to [filename]_downloads
# The filename should contain the full URL to the target file(s)

import sys
import os
import urllib.request

instructions =  "download_file_list.py - script to download all the files in a list\n" +\
		"Usage: download_file_list.py [filename]"

if len(sys.argv) <2 or len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
	print (instructions)
	sys.exit()

filename = sys.argv[1]

download_directory = (filename + '_downloads')
if not os.path.exists(download_directory):
	os.makedirs(download_directory, exist_ok = True)
	print("Directory '%s' created successfully" % download_directory)
else:
	print("Downloads directory '%s' already exists or cannot be created" % download_directory)
	exit()

links = open(filename, 'r')
for link in links:
	link = link.strip()
	file = link.rsplit('/', 1)[-1]
	#filename = os.path.join('downloads', name)

	if not os.path.isfile(link):
		print('Downloading: ' + file)
		local_file = './' + download_directory + '/' + file
		try:
			urllib.request.urlretrieve(link, local_file)
		except Exception as inst:
			print(inst)
			print('Encountered unknown error. Continuing.')
