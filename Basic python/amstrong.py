
     
     
num=int(input("Enter Number:"))
add=0
rem=0
temp=num
while(num>0):
     rem=num%10
     add=add+rem*rem*rem
     num=num//10
     
if(temp==add):
     print(temp," is amstrong number")
else:
     print(temp," is not amstrong number")
     
