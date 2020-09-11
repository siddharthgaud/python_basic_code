thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

print(thislist[1])    #Access Item
print(thislist[-1])    #Negative indexing

print(thislist[2:5])    #range of index

print(thislist[:4])
print(thislist[2:])

print(thislist[-4:-1])      #negative indexing

thislist[1] = "blackcurrent"
print(thislist)

for x in thislist:        #loop through a list
    print(thislist)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")   #check if item exist

print(len(thislist))    #Lenght of a list

thislist.append("siddharth")    #append
print(thislist)

thislist.insert(1,"dddd")       #insert
print(thislist)

thislist.remove("dddd")
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

#thislist.clear()
#print(thislist)

mylist = thislist.copy()
print(thislist)

mylist = list(thislist)
print(thislist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)

list1.extend(list2)
print(list1)

thislist = list(("apple", "banana", "cherry"))     # note the double round-brackets
print(thislist)


































