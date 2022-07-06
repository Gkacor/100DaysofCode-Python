choice1 = input("You are in a unknown island enjoying vacation. You decided to do a little run in the morning,"
                " and now you are lost. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You found a hole filled with water that could lead you back home."
                    " Do you want to try and swim or do you wait? Type 'swim' or 'wait': ").lower()
    if choice2 == "wait":
        choice3 = input("You waited a little, then swam into the hole and found an undiscovered cave inside,"
                        " now there's three doors. "
                        "Which door do you choose? Type 'red', 'blue or 'yellow': ").lower()
        if choice3 == "red":
            print("You got inside a burning room, and the fire burned you to death. GAME OVER.")
        elif choice3 == "blue":
            print("There were a dozen beats inside, and you've just unlocked their cell. They've eaten you. GAME OVER.")
        elif choice3 == "yellow":
            print("You open the yellow door, cautiously, and inside there's an enormous treasure. YOU WIN!")
        else:
            print("You took too long to choose, the ground opened and you fell, hitting you head. GAME OVER.")
    else:
        print("You've been attacked by a beast inside the hole, if you've had waited,"
              " the beast would've' been gone. GAME OVER.")
else:
    print("You found a dangerous forest, and now you are more lost than ever. GAME OVER.")