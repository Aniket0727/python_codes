class Boss:
    def report(self):
        print("Mich ahe Boss")

class Manager1(Boss):
    def report(self):
        print("Manager1:Report to boss")

class Manager2(Boss):
    def report(self):
        print("Manager2:Report to boss")
        
class TeamLead1(Manager2,Manager1):
    def report(self):
        print("TeamLead1:Report")

class TeamLead2(Manager2,Manager1):
    def report(self):
        print("TeamLead2:Report")   
        
class Developer(TeamLead2,TeamLead1):
    def report(self):
        print("Developer")
        
obj=Developer()
obj.report()

# print(Developer.mro())
print(Developer.__mro__)