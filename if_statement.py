is_male = False
is_tall= False

if is_male and is_tall:
    print("You're a Tall Male")
elif is_male and not(is_tall):
    print("You're a short Male")
elif not(is_male) and is_tall:
    print("You're not a male but tall")
else:
    print("You're not a Male or Not Tall")
