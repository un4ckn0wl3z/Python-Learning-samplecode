class Family(object) :
    
    pid = 0
    
    def __init__(self, firstname, lastname, age, status) :
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.status = status
        Family.pid = Family.pid + 1
        
    def displayFaminfo(self) :
		print "Id : %d , Name : %s , Lastname : %s , Age : %s , Status : %s !" % (Family.pid, self.firstname, self.lastname, self.age, self.status)
        
        
    def stockFamily(self) :
        conid = str(Family.pid)
        txt = "infosf.txt"
        target = open(txt, 'a')
        target.write("Id : " + conid + ", Name : " + self.firstname + ", Lastname : " + self.lastname + ", Age : " + self.age + ", Status : " + self.status + "\n")
        target.close
        
    
        


loop = True

while loop :
    print """
    ==========================================
    SIMPLE FAMILY INFORMATION
    by bl@$t_en3my
    ==========================================
    """ 
    print "Please enter your INFORMATION."
    firstname = raw_input("Name : ")
    lastname = raw_input("Lastname : ")
    age = raw_input("Age : ")
    status = raw_input("Status : ")
    
    Person = Family(firstname, lastname, age, status)
    Person.displayFaminfo()
    Person.stockFamily()

    print "Do you want to field other..."
    print "Y = Yes"
    print "N = No"
    
    next = raw_input("> ")



    if next == "y" :
        loop = True
    else :
        loop = False
































