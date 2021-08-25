#!/usr/bin/python3

# Script to query date/month/year docs from a website

import requests

day = 1 
month = 1 
year = 2020

def url_ok(url):
	r = requests.head(url)
	return r.status_code

while year < 2021:
	date = str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
	url = "http://intelligence.htb/documents/" + date + "-upload.pdf"
	url_status = url_ok(url)
	if url_status == 200:
		print(url + "\t" + "Document Exists")
	day += 1
	if day > 31:
		day = 1
		month += 1
	if month > 12:
		month = 1
		year += 1
