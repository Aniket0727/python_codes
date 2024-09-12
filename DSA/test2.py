l=[]
import sys

for i in range(100):
    print(i,sys.getsizeof(l))
    l.append(i)
