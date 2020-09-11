print("Hello")
print('Hello')

#assign string to a variable
a = "Hello"
print(a)

#Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#String are arrays
a = "Hello, World!"
print(a[1])

#Slicing
b = "Hello, World!"     #starts from 2 to 8 but 8 is excluded means till 7
print(b[2:8])

#Negative Indexing     #starts from -2 to -5 but -5 is excluded means till -4
b = "Hello, World!"
print(b[-5:-2])

#String Length
a = "Hello, World!"
print(len(a))

#String Methods
x = " Hello, World!  " #The strip() method removes any whitespace from the beginning or the end:
print(x.strip())

#lower
a = "Hello, World!"
print(a.lower())

#upper
a = "Hello, World!"
print(a.upper())

#Replace
a = "Hello, World!"
print(a.replace("H", "J"))

#Check string
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt   #Not in also present next to in
print(x)

#string Concatenation
a = "Hello"
b = " World"
c = a + b
print(c)

#string format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


























