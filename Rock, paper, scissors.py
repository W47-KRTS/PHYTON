# rock, paper, scissors game

import random

myList = ['rock', 'paper', 'scissors']

rez_PC = random.choice(myList)  # results random one of 3 values-result PC

a, b, choice_Human = "", "", "",

while len(a) == 0:
    a = input("Hello! What is your name? ")

print(f"Well, hello mister, {a}! Wanna play a little game?")

while len(b) == 0:
    b = input("Please answer with yes or no? ").lower()

if b == 'yes':
    while not (choice_Human == myList[0] or choice_Human == myList[1] or choice_Human == myList[2]):
        choice_Human = input(f"Perfect,{a}, please choose between:{myList}: ").lower()
elif b == 'no':
    print(f"That's unfortunate, mister {a}. Bye, bye!"), exit()
else:
    while not (b == 'yes' or b == 'no'):
        b = input("Please answer with yes or no? ").lower()

if not choice_Human == 0:
    print(f"Well, then, my choice is {rez_PC}, so... ")

if rez_PC == myList[0] and choice_Human == myList[0]:
    print(f"Hmm, I guess this is a draw, mister {a}. Let's try again, shall we?")
elif rez_PC == myList[0] and choice_Human == myList[2]:
    print(f"I am truly sorry, mister {a}. It seems you've lost. Let's try again!")
elif rez_PC == myList[0] and choice_Human == myList[1]:
    print(f"But this cannot bee!!! Mister {a}, it seems you have won!")
else:
    if rez_PC == myList[1] and choice_Human == myList[1]:
        print(f"Hmm, I guess this is a draw, mister {a}. Let's try again, shall we?")
    elif rez_PC == myList[1] and choice_Human == myList[0]:
        print(f"I am truly sorry, mister {a}. It seems you've lost. Let's try again!")
    elif rez_PC == myList[1] and choice_Human == myList[2]:
        print(f"But this cannot bee!!! Mister {a}, it seems you have won!")
    else:
        if rez_PC == myList[2] and choice_Human == myList[2]:
            print(f"Hmm, I guess this is a draw, mister {a}. Let's try again, shall we?")
        elif rez_PC == myList[2] and choice_Human == myList[1]:
            print(f"I am truly sorry, mister {a}. It seems you've lost. Let's try again!")
        elif rez_PC == myList[2] and choice_Human == myList[0]:
            print(f"But this cannot bee!!! Mister {a}, it seems you have won!")
        else:
            exit()
