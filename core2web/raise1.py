class VotingError(Exception):
    
    def __init__(self,msg):
        super().__init__(msg)
        # print(msg)

def voting(name,age):
    
    if age<18:
        raise VotingError("Not eligible")
    else:
        print("thanks")
        
print("start code")
name=input("Enter name: ")

try:
    age=int(input("Enter age: "))
except ValueError:
    print("add integer data")
    age=int(input("Enter age: "))
    
try:
    voting(name,age)
except VotingError as e:
    print(e.msg)
    
print('End Code')