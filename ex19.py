def cheese_and_crackers(cheese_count, boxes_of_crackers) :
    print "You have %d cheese !" % cheese_count
    print "You have %d boxes of crackers !" % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly : "
cheese_and_crackers(20, 30)

print "OR, can just give variable from our script : "
amout_of_cheese = 10
amout_of_crackers = 50

cheese_and_crackers(amout_of_cheese, amout_of_crackers)

print "We can even do math inside too : "
cheese_and_crackers(10 + 50,  5 + 6)

print "And we can combine the two, variable and math : "
cheese_and_crackers(amout_of_cheese + 100,  amout_of_crackers + 100)





