thisdict ={
    "brand" : "ford",
    "model" : "mustang",
    "year" : "1964"
}
print(thisdict)

'''x = thisdict["model"]
y= thisdict.get("brand")
print(x)
print(y)

thisdict["year"] = 2018
print(thisdict)

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

if "model" in thisdict:
    print("yes! model is present this dictionaries")
else:
    print("not present")

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("color")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)'''

mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)































