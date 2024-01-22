num1 = int(input("Enter a Number: "))
op = input("Enter an Operator: ")
num2 = int(input("Enter a Number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")