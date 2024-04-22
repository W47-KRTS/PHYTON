import random 

top_of_range = (input("Type a number: "))

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Insert number bigger than 0!")
        quit
else:
    print("Type a number!!!")
    quit()

random_number = random.randint(0, top_of_range) # randint includes max nb

guessed = 0 

while True:
    guessed += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number!!")
        continue

    if user_guess == random_number:
        print("That s right!!")
        break
    elif user_guess > random_number:
        print("Try again a smaller number!")
    else:
        print("Try again a bigger number!")

if guessed == 1:
    print(f"You got it in {guessed} attempt, you're the man!!")
else:
    print(f"You got it in {guessed} attempts, good job!")    