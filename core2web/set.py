s1=set()

s1={11,True,"True"}
print(s1)
print(type(s1))

s1.add(10)
print(s1)
print()
s2=frozenset([1,2,3,4,5])
print(s2)

s2.add(10)
print(s2)


s3={1,2,3,4,5}
s4={6,7,2,1,8}
s6={6,7}
print(s3.difference(s4))
print(s3.difference_update(s4))

print(s3)
print(s4)
print(s3.discard(6))

print(s3.isdisjoint(s4))  #if some data is same then it return false 
print(s6.issubset(s4))


s5=s3.intersection(s4)  #same element shows
s6=s3.symmetric_difference(s4)
s7=s3.union(s4)
print(s6.update(s4))
print(s5)
print(s6)
print(s7)


s8={1,2,3,4,5}
print(s8.pop())
print(s8.remove(1))
print(s8)
print(s8.clear())
print(s8)