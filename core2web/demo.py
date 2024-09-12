def outer_func(x, y):
    def inner_func(m, n):
        return m + n

    return inner_func(x, y)
    return x


obj=outer_func(5,10)
print(obj.mro())