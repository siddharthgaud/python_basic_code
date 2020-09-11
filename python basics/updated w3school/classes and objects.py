class myclass:           #creating myclass
    x = 5
print(myclass)
p1 = myclass()            #creating object
print(p1.x)

class person:
    def __init__(self, name, age):         #__init__ function
        self.name = name
        self.age = age
p2 = person("siddharth",23)
print(p2.name)
print(p2.age)

class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(mysillyobject):                   #any attribute othr than self is valid
        print("Hello my name is "+mysillyobject.name+" and i am " +str(mysillyobject.age)+" years old")
p3 = person1("siddharth",23)
p3.myfunc()
















