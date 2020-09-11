x = "siddharth"
y = "23"
print(x)
print(y)

x = "23"
x = "siddharth"
print(x)

x,y,z = "apple","mango","banana"
print(x)
print(y)
print(z)

x=y=z= "orange"
print(x)
print(y)
print(z)

x= "awesome"
print("python is "+x)

x= 5
y = 10
print(x +y)

print("**********Global variables************************")
x = "awesome"
def my_func():
    print("python is "+x)
my_func()

y = "Great"
def func():
    y = "beautiful"
    print("Python is "+y)
func()

print("python is "+y)

def fun():
    global x
    x="fantastic"
fun()
print("python is "+x)

x = "best"
def function():
    global x
    x = "easy"
function()
print("programming is "+x)
