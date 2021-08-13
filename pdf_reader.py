#!/usr/bin/python3

# pdf_reader.py
# A script to read the contents of all the PDF files within the current directory

import PyPDF2
import os

directory = '.' 

for filename in os.listdir(directory):
	if filename.endswith('.pdf'):
		print(filename)
		pdf_file = open(filename, 'rb')
		pdf_reader = PyPDF2.PdfFileReader(pdf_file)
		#page = pdf_reader.getPage(0)
		number_of_pages = pdf_reader.getNumPages()
		for page_number in range(number_of_pages):
			page = pdf_reader.getPage(page_number)
			page_content = page.extractText()
			print(page_content)
pdf_file.close()
