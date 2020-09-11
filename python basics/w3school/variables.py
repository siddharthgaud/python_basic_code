# indentation  comments  and variables
#simple hello world
print("hello world")

#indention program
if (5>2):
    print("five is greater than two")
print("five is greater than two outside the block")
if (5<10):
            print("five is less than ten")
print("five is less than ten outside the block")

#variables
x= 5
x = "x is now changed from 5"
y = "hello World"
print(x)
print(y)

x,y,z = "apple","mango","banana"
print(x)
print(y)
print(z)

x=y=z="apple"
print(x)
print(y)
print(z)

x="awesome"
print("python is "+x)

x="awesome"
y="python is "
z = y + x
print(z)

x = 5
y = 10
print(x + y)

x = "fantastic!!!"      #global variables >>variable is defined outside the function
def my_func():
    print("python is "+x)
my_func()

y = "awesome   global variable"           #global variable
def my_func():
    x = "fantastic   local variable "      #local variables
    print("python is "+x)
my_func()
print("python is "+y)

def my_func():    #for making local variable as global use global keyword
    global a      #now variable can be use outside the function
    a = "easy"
my_func()
print("python is "+a)

a = "understandable" #use the global keyword if you want to change a global variable inside a function.
def my_func():
    global a
    a = "interactive"
my_func()
print("python is "+a)



