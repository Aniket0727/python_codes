def fun(x,y):  #2
    print("Start fun")
    while(x<=y):  #3  #8
        yield x   #4  #9
        x=x+1   #7
    print("End fun")
    
for val in fun(1,10):  #1  #5(line 4 x value store in val) #10
    print(val)   #6 go to line no 7    #11
    