x = "Hello world "
print(x)
print(x[1])
print(x[2:7])
print(x[-5:-2])
print(len(x))
print(x.strip())
print(x.lower())
print(x.upper())
print(x.replace("H","J"))
print(x.split(","))
if "ellom" not in x:
    print("yes")
else:
    print("No")

name = "siddharth"
age = 23
txt = "my name is {0} and i am {1} years old"
print(txt.format(name,age))


