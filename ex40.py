class Comgeeks(object) :
    def __init__(self, hacker, cracker):
        self.hacker = hacker
        self.cacker = cracker
        
    def displaymeanofgeeks(self) :
        print "I love ", self.hacker
        print "I hate ", self.cacker
        
obj = Comgeeks("Hacker very much", "Cracker fuck them out")
obj.displaymeanofgeeks()