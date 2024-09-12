s1="Python"
print(s1)
print(type(s1))
print(len(s1))

s2='''Java
Python
HTML'''
print(s2)
print(type(s2))
print(len(s2))

s3="Python is '''power''' full language"
print(s3)

s4="Python is \power\n full  language"
print(s4)

s5=r"Python is \power\n full  language"
print(s5)

s6="\u0906 \u0908"  # unicode format
print(s6)

s7="python is power"
s8="Java"
s9="java"
print(s7[0::2])
print(s7.count('a'))

print(s7.capitalize())
print(s8.casefold()==s9.casefold()) #first letter convert into small letter
print(s8.center())

s10="Python is \t programming langugae"
print(s10)
print(s10.expandtabs(8))

s11=input("Enter main string: ")
s12=input("Enter find/sub string: ")
 

if s11 in s12:
    print(s12," is found")
else:
    print(s12," is found")

n=s11.find(s12)  # if not found find() return -1
n=s11.rfind(s12) #rfind() find in right side 
print(s12+" found at {}".format(n))
    
    
s13="123"    
print(s13.isdigit())
print(s13.isdecimal())

s14="Python is programming language"
print(" . ".join(s14))

s15="Python"
print(s15.ljust(8,"#"))
print(s15.rjust(8,"#"))

s16="   Python  "
print(s16)
print(s16.strip())
print(s16.rstrip())
print(s16.lstrip())


s17="PythonisPrograming"
print(s17.partition("is"))
print(s17.partition("nothing"))
print(s17.rpartition("not"))

s18="Python,is,Programing"
print(s18.split("P"))


x,y,z=[int(val) for val in input("Enter Number: ").split(",")]
print(x+y+z)
