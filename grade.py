
try:
    score = int(input("Score: "))
    if isinstance(score, str):
        print("Input a number")
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score <= 90:
        print("Grade: B")
    elif 70 <= score <= 80:
        print("Grade: C")
    elif 60 <= score <= 70:
        print("Grade: D")
    else:
        print("Grade: F")
except ValueError: 
    print("Score Must Be a Number")