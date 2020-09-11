"""a = 10
b = "siddharth"
a = "Gaud"
print(a)
print(b)

a=b=c = "apple"
print(a)
print(b)
print(c)

x= "awesome and "
y  = "fantastic"
z = x +y
print("python is " +z)

x = 5
y = 10
z = x +y
print(z)

y= "awesome"

def myfunc():
    global y
    y = "easy"
    print("python is "+y)
    print("python is "+y)
myfunc()
print("python is "+y)
print("python is "+y)

p = "forever"
q = 99
print(p +str(q))"""

name = "siddharth"       #global variable works inside and outside of a function

def func():
    global y       #local to global use  global keyword
    y = "young"          #local variable only works inside of a function
    print("my name is "+name)
    print("siddharth is "+y)
func()
print(name+ " is my name")
print("He is "+y)

f = 11           #del variable
print(f)
del f
print(f)
