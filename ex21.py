def add(a, b) :
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b) :
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b) :
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b) :
    print "DEVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just function"

age = add(18, 1)
height = subtract(170, 5)
weight = multiply(10, 5)
iq = divide(1000, 10)


print "Age : %d, Height : %d, Weight : %d, IQ : %d" % (age, height, weight, iq)

print "Here is puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes : ", what, "Can you do it by hand ?"




















