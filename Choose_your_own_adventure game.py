# Choose your own adventure game 

name = input("Type your name: ")

answer = input("You are on a road and it has come to crossfork. You can choose to go left or right. Or go back ")

if answer == "left":
    answer = input("You find a chest. Open or continue to walk? ")
    if answer == "open":
        print("A treasure, you are rich. But how to carry it? Well that is another story.")
        quit()
    elif answer == "continue to walk": 
        print("YOu walk and you walk and you walk...")
        quit()
    else:
        ("You are annoying. Story is over")   
        quit()

elif answer == "right":
    answer = input("You come to a river. Walk around or swim across? ")
    if answer == "swim":
        answer = input("You encounter an alligator. You run or fight? ") 
        if answer == "run":
            print("The scars on the back are a worriors greatest shame. YOu DIE!")
        elif answer == "fight":
            print("YOu die. But not alone, you take the gator with you.")
        else:
            ("You are annoying. Story is over")
            quit()
    elif answer == "walk around":
        answer = input("You find a big tree. Sit under it or continue to walk? ")
        if answer == "sit under it":
            print("YOu fell asleep. Who just sleeps under a tree, you weirdo?")
        elif answer == "continue to walk":
            print("YOu walk and you walk and you walk...")
    else: 
        print("Swim or walk around...")
elif answer == "go back":
    print("Sure, going back sounds good. You won!!")
else:
    print("Left or right...")

print("Goodbye, mr. 47")
    