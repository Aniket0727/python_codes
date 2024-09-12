user_list = [item.strip() for item in input("Enter values separated by commas: ").split(' ')]


n= input("Enter Num: ")
if n in user_list:
    print("found")
else:
    print("not found")