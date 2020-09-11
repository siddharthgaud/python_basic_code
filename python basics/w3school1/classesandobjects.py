'''class myclass:             # classes and object
    x = 5
p1 = myclass()

print(p1.x)'''

'''class person:               # _init_ function
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("siddharth",23)
print(p1.name)
print(p1.age)'''

'''class person:               #object as method
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1 = person("siddharth",23)
p1.myfunc()'''

class person:                               # self parameter
    def __init__(mysilliobject,name):
        mysilliobject.name = name
        mysilliobject.age = age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1 = person("siddharth")
p2= person(23)
p2.age = 40
print(p2.age)





