from sys import argv

script, filename = argv

print "I want to read my last file I wrote, %s," % filename
file = open(filename)
print file.read()

file.close()




