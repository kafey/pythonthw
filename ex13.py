from sys import argv

script, first, second, third = argv

print "The script is called:" , script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variabel is: ", third

raw_input("what is your favorite %s? " % (first))
raw_input("what is your favorite %s ? " % (second))
raw_input("What %s do you live? " % (third))
