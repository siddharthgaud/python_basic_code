#create a class
class myclass:
    x = 5
print(myclass)
#create an object
p1= myclass()
print(p1.x)
#the _init_ func()
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class persons:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("siddharth",23)
p2 = persons("daksha",20)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print("###############################################333")
#object and methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and my age is "+str(self.age))
    print("my age is "+str(self.age))

p1 = Person("siddharth", 23)
del p1.age
print(p1.age)
p1.myfunc()

