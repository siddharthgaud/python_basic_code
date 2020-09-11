#Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#When you run a condition in if statement it returns true or false
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate values and variables
print(bool("Hello"))
print(bool(15))

#Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#most value are true and
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# some values are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#function can return a boolean
def myFunction() :
  return True

print(myFunction())

#isinstance() function, which can be used to determine if an object is of a certain data type:
x= 200
print(isinstance(x, int))
