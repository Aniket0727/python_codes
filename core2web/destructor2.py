class parent:

    def __init__(self):
        print("In constructor parent")  
    
    def __del__(self):
        print("In destructor")  

obj1=parent()
obj1=parent()
print("Code samplay")


# Output
# In constructor parent  -1
# In constructor parent  -2
# In destructor          -3
# Code samplay           -4
# In destructor          -5

# line 1,2 print because 2 objects are created(when we are creating 2 object that time init method called automatically 2 time ) 
# 1st obj1 destroy because 2nd obj overlap on 1st obj that time when 1st obj destory that time it called automatically destructor(__del__())
# so print "In destructor" message but 2nd obj not deleted because code are reamins then it print last message "Code samplay" all code are excuted and 
# then 2nd obj are destroy and called automatically destructor(__del__()) function.
