x = 5
y = "siddharth"
x = "variable value can be changed"
print(x)
print(y)

a , b ,c = "apple","banana","orange"
print(a)
print(b)
print(c)

e = f = g = "apple"
print(e)
print(f)
print(g)

x = "wounderful"
print("python is "+x)

'''x = 5
y=  "sid"
print(x +y)'''

#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

x = "fantastic"        #global  variable

def func():
    print("python is " +x)
func()
print("python is "+x)

x = "awesome"        #Global variable
def func1():
    x = "easy"       #local variable
    print("python is "+x)
func1()
print("python is "+x)

def func3():
    global x            #global keyword to make local variable to global variable
    x = "ready"
func3()
print("python is "+x)

x = "siddharth"

def func4():
    global x             #Also, use the global keyword if you want to change a global variable inside a function.
    x = "daksha"
func4()
print("my name is "+x)









