thislist = ["apple","banana","cherry","orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[0])         #access items using index
print(thislist[-2])        #negative indexing
print(thislist[2:5])       #range of index        2 include    5 exclude
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])      #    -4 included    -1 excluded
thislist[1] = "blackcurrant"  #change item values
print(thislist)
for x in thislist:        #Loop Through a List
    print(x)
if "apple" in thislist:
    print("yes it exist")     #check if item exist
print(len(thislist))
thislist.append("orange")       #add items
print(thislist)

thislist.insert(1, "orange")
print(thislist)

thislist = ["apple","banana","cherry","orange", "kiwi", "melon", "mango"]
thislist.remove("banana")
print(thislist)

thislist.pop()
print(thislist)

'''del thislist[0]
print(thislist)

thislist.clear()
print(thislist)'''

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)




