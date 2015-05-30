# request function argv from library sys
from sys import argv
# input in cli when running the code $pyhton ex15.py ex15_sample.txt
script , filename = argv
# open file ex15_sample.txt
txt = open(filename)
# print the file
print "Here's your life %r" % filename
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

