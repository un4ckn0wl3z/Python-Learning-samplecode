from sys import exit

def new_line() :
    for num in range(first_num, last_num) :
        print num
        numtxt = str(num)
        target_txt.write(numtxt + "\n")

def space_line() :
    for num in range(first_num, last_num) :
        print num
        numtxt = str(num)
        target_txt.write(numtxt + " ")

print """
####################################
  AUTOMATE GENERATE NUMBER LIST
                    by bl@$t_en3my
####################################
"""

first_num = int(raw_input("Enter first number : "))
last_num = int(raw_input("Enter last number : "))


print "We will generate number %d to %d !!" % (first_num, last_num)
print "Enter to continue. CTRL-C to exit.",
raw_input()

last_num += 1
txt = "list.txt"

target_txt = open(txt, 'w')

print "Choose your write mode : "
print "1.New line."
print "2.Space line."

mode = raw_input("> ")

if mode == "1" :
    new_line()
elif mode == "2" :
    space_line()
else :
    print "Pleaes choose your mode again."
    exit(0)

target_txt.close()
print "Success!!! Please check a %r file" % txt
