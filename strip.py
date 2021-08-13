#!/usr/bin/python3

import os.path
import sys

# A script to remove white-space from the start and end of a list of words

instructions =  "strip.py - a simple white-space removal script\n" +\
		"Usage: strip.py [filename]"

if len(sys.argv) <2 or len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
        print (instructions)
        sys.exit()

filename = sys.argv[1]
file_to_strip = open(filename, 'r')
for line in file_to_strip:
	line = line.strip()
	print(line)
