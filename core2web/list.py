# l1=[num for num in range(1,10)]
# # print(l1)

# l2=["Annu","Aniket",["Omkar","Yash"]]
# print(l2)


# l2[1]="Rushi"

# print(l2)

# shallow copy
# l3=["Java","Python","Programing in c",["HTML","PHP","CSS"]]

# l4=l3.copy()

# print("l3: ",l3)
# print("l4: ",l4)

# l3[3][1]="BOOTSTRAP"
# print("After Change ")
# print("l3: ",l3)
# print("l4: ",l4)


# deep copy

# l5=["Java","Python","Programing in c","HTML","PHP","CSS"]

# l6=l5.copy()

# print("l3: ",l5)
# print("l4: ",l6)

# l5[3]="BOOTSTRAP"
# print("After Change ")
# print("l3: ",l5)
# print("l4: ",l6)



import copy as cp
l7=["Java","Python","Programing in c",["HTML","PHP","CSS"]]

l8=cp.deepcopy(l7)
# l8=l7.copy()


print("l7: ",l7)
print("l8: ",l8)

l7[3][1]="BOOTSTRAP"
print("After Change ")
print("l7: ",l7)
print("l8: ",l8)