def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max(300, 2, 3))


try:
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if isinstance(x, str) or isinstance(y, str):
        print("Error: x or y must be a number")
    elif x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print(f"x equals y: {x}")
except ValueError:
    print("Please enter valid integers for x and y.")
