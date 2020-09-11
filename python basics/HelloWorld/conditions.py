is_hot = False
is_cold =False

if is_hot:
    print("its a hot day")
    print("drink plenty of water")
if is_cold:
    print("its a cold day")
    print("wear warm clothes")
else:
    print("its awesome day")

#if statement
i = 10
if i>25:
    print("i is greater than 15")
print("good")

#if-else statement
a = 20
if a>25:
    print("a is greater than 25")
    print("i am in if block")
else:
    print("a is lesser than 25")
    print("i am also in if block")
print("i am not in if block")

# if-else statement
i = 20
if i>20:
    print('i si greater than 20')
else:
    print("i is equal to 20")

#nested if statement
b = 4
if b>5:
    print("b is greater than 5")
if b>6:
    print("b is greater than 6")
if b>7:
    print("b is greater than 7")
else:
    print("b is less than 5")

#if elif else statement
i = 20
if i==10:
    print("i is 10")
elif i==15:
    print("i is 15")
elif i==20:
    print("i is 20")
else:
    print("i is not present")

 #exercise
name = "siddharth"
if len(name)<3:
     print("name should be atleast three character")
elif len(name)>50:
     print("name should not be greater than fifty character")
else:
     print("name looks good")


#Guessing number
number = int(input("guess any number between 1 to 10 :"))
if number<2:
    print("too low")
elif number>8:
    print("too high")
else:
    print("right number")






























