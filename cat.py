# i = 1

# while i <= 3:
#     print("meow")
#     print(i)
#     i += 1


# for i in [0, 1, 2]:
#     print("meow", i)


# for i in range(10000):
#     print("meow")

# for _ in range(10000):
#     print("meow")

# print("meow\n" * 200, end="")
 

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#       break

# for _ in range(n):
#    print("meow")

def main():
    number = getNumber()
    meow(number)


def getNumber():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()