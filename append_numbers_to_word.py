#!/usr/bin/python3

import sys

# Simple script to append numbers after a keyword entered on the cmd line

instructions =  "append_numbers_to_word.py - a script to simply append numbers to a word\n" +\
                "Usage: append_numbers_to_word.py [word]"

if len(sys.argv) <2 or len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
        print (instructions)
        sys.exit()

word = sys.argv[1]

for count in range(1, 1000): # Set the number range here i.e. 1 - 999 
	print(word + str(count))
