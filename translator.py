def translate(phrase):
    translation = ""
    for value in phrase:
        if value in "AEIOUaeiou":
        translation = translation + "g"
    else:
        translation = translation + value
        return  translation


print(translate())