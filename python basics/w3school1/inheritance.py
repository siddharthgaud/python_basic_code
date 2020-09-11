'''class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
x = person("siddharth","gaud")
x.printname()

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)

x = student("mikejjj","john")
x.printname()'''

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)
x = person("siddharth","Gaud")
x.printname()

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of ",self.graduationyear)
x = student("mike","john",2019)
x.printname()
print(x.graduationyear)
x.welcome()












