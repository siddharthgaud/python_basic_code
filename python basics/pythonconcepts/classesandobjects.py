class myclass:
    x = "siddharth"
    print(x)

p1 = myclass()
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("sid",23)
p2 = person("jony",56)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
      print("Hello my name is " + self.name)
      print("Hello my age is " + str(self.age))


p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
print(p1.age)

del p1.age
print(p1.age)

del p1
print(p1)

class person1:
    pass

