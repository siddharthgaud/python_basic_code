'''Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview'''

x= 5
print(type(x))

#setting the datatype
a = str("Hello World")  #string
print(a)
print(type(a))

b = int(20)             #integer
print(b)
print(type(b))

c = float(20.5)         #float
print(c)
print(type(c))

d = complex(1j)         #complex
print(d)
print(type(d))

e = list(["apple", "banana", "cherry"])    #list
print(e)
print(type(e))

f = tuple(("apple", "banana", "cherry"))    #tuple
print(f)
print(type(f))

g = range(6)                           #range
print(g)
print(type(g))

h = dict({"name" : "John", "age" : 36})    #dictionary
print(h)
print(type(h))

i = {"apple", "banana", "cherry"}          #set
print(i)
print(type(i))

j = frozenset({"apple", "banana", "cherry"})   #frozenset
print(j)
print(type(j))

k = True                           #boolean
print(k)
print(type(k))

l = b"Hello"                      #byte
print(l)
print(type(l))

m = bytearray(5)                 #bytearray
print(m)
print(type(m))

n = memoryview(bytes(5))          #memoryview
print(n)
print(type(n))



