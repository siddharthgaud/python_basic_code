def my_function():
    print("Hello from function")
my_function()

def function(firstname):
    print(firstname + " Gaud")
function("siddharth")
function("daksha")
function("veena")
function("pramod")

def func(fname,lname):
    print(fname +" "+lname)
func("siddharth","Gaud")
func("Daksha","Gaud")

def fun(*kids):
    print("the youngest kid is "+kids[1])
fun("adc","abcd","abcdef")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_functions(country = "Norway"):
  print("I am from " + country)

my_functions("Sweden")
my_functions("India")
my_functions()
my_functions("Brazil")

def my_fun(foods):
    for x in foods:
        print(x)
fruits = ["apple","mango","banana"]
my_fun(fruits)

def fu(x):
    return 5 * x
print(fu(2))
print(fu(3))
print(fu(4))

def ffunctn():
    pass

def squ(x):
    return x * x
print(squ(5))

'''f = square
def sum_of_square(f,x,y):
    return f(x) + f(y)

print(sum_of_square(square,2,4)'''

'''f(4)
def fxy(f, x, y):
    return f(x) + f(y)
fxy(square, 2, 3)'''

x = 0
y = 0
def incr(x):
    y =x + 1
    return y
incr(5)
print(x,y)

x = 5
def mysquare():
    global x
    x = 4
    print(x)
mysquare()

