# calculator by user input

op = input("enter the operator which you want to use :")
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

if op == "+":
    num3 = num1 + num2
    print("answer " +str(num3))
elif op == "-":
    num4 = num1 - num2
    print("answer " +str(num4))
elif op == "*":
    num5 = num1 * num2
    print("answer " +str(num5))
elif op == "/":
    num6 = num1 / num2
    print("answer " +str(num6))
else:
    print("unexpected result")

