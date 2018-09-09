#!/usr/bin/env python
import fileinput # This module gives us the ability to read files
import re # This imports the regex capability
import sys # this gives us ability to read stdin

compiled_regex = re.compile(sys.argv[1]);  # This takes our regex expression
my_file = sys.argv[2] # This is the input for the name of the file

for each_line_of_text in fileinput.input(my_file):
    matches = compiled_regex.findall(each_line_of_text)
    print matches
