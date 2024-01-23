
try:
    value = 10/0
    numbers = int(input("Enter a number: "))
    print(numbers)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid Input")
