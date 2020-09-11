thisset = {"apple", "banana", "cherry"}
print(type(thisset))

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("kiwi" in thisset)

thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
    print("yes! banana is present")
else:
    print("not present")

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange","kiwi","potato"])
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

'''thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)'''

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

thisset = set({"apple", "banana", "cherry"})
print(thisset)



