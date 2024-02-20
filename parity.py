def main():
    try:
        x = int(input("Input x "))
        if is_even(x):
            print(f"{x} is an even Number")
        else: 
            print(f"{x} is an odd number")
    except ValueError:
        print("X must be a number")
            


def is_even(n):
        # if n % 2 == 0:
        #     return True
        # else: 
        #     return False
    
        # return True if n % 2 == 0 else False

        return n % 2 == 0


    
while True:
    main()
   
