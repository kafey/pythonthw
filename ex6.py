# varible x with  format character %s and integer
x = "There are %d types of people." % 10
# variable binary string
binary = "binary"
# variable do_not string
do_not = "don't"
# varible y 2 format characters %s with multiple variable 
y = "Those who know %s and those who know %s." % (binary, do_not)
# print x and y
print x
print y
# print format character 'r' with variable x and format character 's' with varible y
print "I said: %r." % x
print "I also said: '%s'." % y
# format character '%r'
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# print variable joke_evaluation that contain format character '%r' take variable hilarious
print joke_evaluation % hilarious
# a character variable w and e
w = "This is the left side of..."
e = "a string with a right side."
# join 2 variable string with '+'
print w + e
