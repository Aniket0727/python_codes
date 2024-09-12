
# from program2 import ICC  #from Moule_name import class_name
class BCCI():
    def __init__(self):
        print("BCCI")
        
class IPL(BCCI):
    def __init__(self):
        print("IPL")


if __name__=='__main__':
    IPL()
else:
    BCCI()




# obj=IPL()
# print(IPL.mro())
# print(IPL.__mro__)