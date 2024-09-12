class Manager:
    
    def project(self):
        print("In proejct manager")

class TeamLead1(Manager):
    pass

class TeamLead2(Manager):
    
    def proejct(self):
        print("In project:TeamLead2")
        
class Developer(TeamLead1,TeamLead2):
    def proejct(self):
        print("In project:Developer")
        
obj=Developer()
obj.proejct()

print(Developer.mro())