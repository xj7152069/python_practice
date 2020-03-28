class organism(object):
    def __init__(self):
        super (organism,self).__init__()
        self.groth=True
        self.death=True
        self.lifetime="various" 
    def meaning(self):
        print "make the world colorful"
    
        
class animal(organism):
    def __init__(self):
        super (animal,self).__init__()
        self.move=True
        
class vertebrate(animal):
    def __init__(self):
        super (vertebrate,self).__init__()
        self.size="usually big"
        self.kinds="totally five kinds"
    def example(self):
        print "example of vertebrate: fish, elephant, panda, human and so on"

class mammal(vertebrate):
    def __init__(self):
        super (mammal,self).__init__()
        self.sex="male and female"
        self.rank="the hightest rank of organism on the Earth"
    
class dog(mammal):
    def __init__(self):
        super (dog,self).__init__()
        self.lifetime="usually can't over 20 years"
        self.character="cute"




