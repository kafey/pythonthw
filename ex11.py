print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do your weigh?",
weight = raw_input()

print "Where do you live?"
address = raw_input()

print "What is your job?"
job = raw_input()

print "So, you're %r old, %r tall and %r heavy" % (
    age, height, weight)

print "You live in %s, and work as %s." % (address, job)
