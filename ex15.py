# using library sys function argv
from sys import argv
# argv use 2 argument script and filename
script, filename = argv
# open file .txt
txt = open(filename)
# print filename and use .read() to show content of the file
print "Here's your file %r" % filename
print txt.read()
# using raw_input to load filename
print "I'll also ask you to type it again:"
file_again = raw_input("> ")
# open file that name input by user
txt_again = open(file_again)
# show the content again with .read() function
print txt_again.read()

