#Basic guess a number in three tries game

gold_number = 6
guess_count =0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number between 0 and 9: "))
    guess_count += 1
    if guess == gold_number:
        print("Hurraah, you are lucky !!!")
        break
else:
    print("Sorry, you did not guess the gold number. Please give it another go. Good Luck!")