print(10>5)
print(10==5)
print(10<5)

print(bool("Hello"))
print(bool(23))

class myclass():
    def __len__(self):
        return  0
myobj = myclass()
print(bool(myobj))

def myfunction():
    return True
print(myfunction())


def function():
    return True

if function():
    print("YES")
else:
    print("FALSE")

x = 200.0
print(isinstance(x,float))

