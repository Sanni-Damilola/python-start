def translate(phrase):
    translation = ""
    for value in phrase:
        if value.lower() in "aeiou":
            if value.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + value
    return translation

print(translate(input("Enter A Word ")))
