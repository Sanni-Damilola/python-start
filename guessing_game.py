secret_word = "games"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while secret_word != guess and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses! 😞 You lose!")
else:
    print("You Win! 💥")
