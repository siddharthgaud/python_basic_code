'''x = " Hello World "
print(x.strip())
print(x.lower())
print(x.upper())
print(x.replace("H","S"))
print(x.split(","))
y= "ello" in x
print(y)'''

'''age = 23
txt = "my name is siddharth, and i am {} years old"
print(txt.format(age))'''

'''a = 332
b = 33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")'''
'''a = 333
b= 45
print("A") if a>b else print("B")'''

'''i = 0
while i<6:
    i += 1
    if i == 3:
        continue
    print(i)'''

'''i = 0
while i<6:
    print(i)
    i +=1'''

'''i= 0
while i < 6:
    print(i)
    if i ==3:
        break
    i +=1'''


'''def myfunc(fname,lname):
    print(fname +" " +lname)
myfunc("siddharth","gaud")'''

'''price = 49
txt = "the price is {:.4f} dollars"
print(txt.format(price))'''


'''name = input("enter your name :")
print("your name is "+name)'''

'''try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("Something else went wrong")
'''

'''try :
    print(x)
except:
    print("something went wrong")
finally :
    print("The try except block is finished")'''

'''import mymodule
mymodule.greeting("siddharth")'''

'''f = open("demofile.txt", "r")

print(f.read())

f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())'''

'''f = open("myfile.txt", "x")'''
'''import os
os.remove("myfile.txt")'''


#print(int(input("enter Your First Number")) * int(input("Enter Second Number")))

'''x = 45
y = 45
print(str(x) + " " +str(y))'''

'''num = input("enter your number :")
print("you entered :" ,int(num )+ 10)'''

'''dict ={"al" : "abc","b":"xyz"}                    important

print("enter the word :")
a = input()
print(dict[a])'''

'''body={
"Hand":"हाथ",
"Leg":" पैर",
"Neck":"गर्दन",
"Skull":"खोपड़ी",
"Head":"सर",
"Finger":"उंगली",
"Nose":"नाक",
"Eye":"आंख",
"Ear":"कान",
"Cheek":"गाल",
"Lip":"होंठ",
"Thumb":"अंगूठा",
"Nail":"नाखून",
"Chest":"छाती",
"Heart":"दील",
"Brain":"दिमाग",
"Liver":"कलेजा",
"Bone":"हड्डी",
"Knee":"घुटना",
"Arm":"कोहनी",
"Shoulder":"कंधा",
"Hair":"बाल",
"Back":"पीठ",
"Forehead":"माथा",
"Lobe":"लोई",
"Palm":"हथेली",
"Foot":"तलवा",
"Face":"चेहरा",
"Tongue":"ज़बान",
"Teeth":"दांत",
"Belly":"पेट",
"Eyebrow":"भौंरे",
"Toe":"टखना",
"Heel":"ऐड़ी",
"Kidney":"गुर्दा",
"Intestine":"अन्तड़ि",
"Lung":"फेफड़े",
"Thigh":"जांग",
"Nostril":"नथुना",
"Jaw":"जबड़ा",
"Navel":"नाभि",
"Axilla":"बगल",
}
print("Enter body part name : ")
a = input()
print(body[a.capitalize()])'''

'''var1 = 10
var2 = 20

var3 = int(input())

if var3 > var2:
    print("greater")
else:
    print("lesser")'''

'''list = [1,2,3,4,5,6,78,9]                          important

a = int(input("enter the number :"))
if a in list:
    print("yes in the list")
else:
    print("not in the list")
    print("try next number")'''

'''age = int(input("enter the age :"))                 challenge

if age > 18:
    print("you can drive")
elif age == 18:
    print("cant decide")
else:
    print("you cant drive")'''














