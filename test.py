# num1,num2=(input().split())

# print(num1)
# print(num2)

# # for i in num:
# #     if (num.index(i)==0):
# #         print("Monday: ",i)
# #     elif(num.index(i)==1):
# #         print("Tuesday: ",i)
# #     elif(num.index(i)==2):
# #         print("Wednessday: ",i)
# #     elif(num.index(i)==3):
# #         print("Thursday: ",i)
# #     elif(num.index(i)==4):
# #         print("Friday: ",i)
# #     elif(num.index(i)==5):
# #         print("Saturday: ",i)
# #     elif(num.index(i)==6):
# #         print("Sunday: ",i)

# s1=set()
# print(type(s1))



import time

# a = [5, 3, 2, 7, 6,9,8,10,0,22,45,67,87]

# # Start time measurement
# start_time = time.time()
# print(start_time)

            
n=6
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()
        