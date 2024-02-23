
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What x? "))
            print(" ")
        except ValueError:
            print("x is not a number")
        else: 
            break
    return  x
    


main()