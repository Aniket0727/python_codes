#Dictionary

dict1={45:"anu",10:"abhi"}

print(dict1)

dict1[50]=dict1.pop(45)
print(dict1.keys())
print(dict1.values())

dict1.clear()

for key,value in dict1.items():
    print(key,".",value)

dict3={45:"anu","abhi":{1:"a"}}
print(dict3)

dict4=dict3.copy()
print(dict4)
print("After chnage")
dict3[45]="aniket"
print(dict3)

print(dict4)

print(dict1["abhi"])

dict2={45:"anni","abhi":{11:"aniket",12:"rahul"}}

print(dict2[1][0])

print(dict2.get(45))


dict5={45:"anu",10:"abhi"}
dict6={5:"anu",1:"abhi"}


dict5.update(dict6)

dict5.setdefault(20,"ankit") #if this key is not present then this key add in dict
print(dict5)

dict7={}
dict6=["Java","Python","Html"]
val="anu"

print(dict7.fromkeys(dict6,val))

print("51")



dict7={}
dict6=["Java","Python","Html"]
val="anu"

print(dict7.fromkeys(dict6,val))

print("51")
dict7={}
dict6=["Java","Python","Html"]
val="anu"

print(dict7.fromkeys(dict6,val))

print("51")
dict7={}
dict6=["Java","Python","Html"]
val="anu"

print(dict7.fromkeys(dict6,val))

print("51")
if():
    pass