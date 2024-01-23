
try:
    value = 10/0
    numbers = int(input("Enter a number: "))
    print(numbers)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
