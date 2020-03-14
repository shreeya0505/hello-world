x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
print "I said: %r." % x    # String in a string
print "I also said:  '%s'." % y		# String in a string

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"	# String in a String

print joke_evaluation % hilarious	# String in a string

w = "This is the left side of..."
e = "a string with a right side."

print w + e