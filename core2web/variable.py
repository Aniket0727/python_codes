class Demo:
    
    z=30  #public
    def __init__(self):
        self._x=10  #protected
        self.__y=20  #private
        # print(self.__y)


# print(dir(Demo))
obj=Demo()
# print()
# print(dir(obj))


print(obj.z)
print(obj._x)
# print(obj.__y)
print(obj._Demo__y)

        