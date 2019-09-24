moves = 0

passcode = 'SSNWES'
userPasscode = ""
won = False

while moves < 30:
    userInput = input("You are in the magic maze. Which way do you want to go? ")
    moves = moves + 1

    userPasscode = userPasscode + userInput
    print(userPasscode)

    if userPasscode[0] == passcode[0]:
        print("you got the first one right")

        userInput2 = input("You are in the magic maze level 2. Which way do you want to go? ")
        userPasscode = userPasscode + userInput2
        moves = moves + 1

        if userPasscode[1] == passcode[1]:
            print("you got the second one right")

            userInput3 = input("You are in the magic maze level 3. Which way do you want to go? ")
            userPasscode = userPasscode + userInput3
            moves = moves + 1

            if userPasscode[2] == passcode[2]:
                print("you got the third right")

                userInput4 = input("You are in the magic maze level 4. Which way do you want to go? ")
                userPasscode = userPasscode + userInput4
                moves = moves + 1

                if userPasscode[3] == passcode[3]:
                    print("you got the 4th one right")

                    userInput5 = input("You are in the magic maze level 5. Which way do you want to go? ")
                    userPasscode = userPasscode + userInput5
                    moves = moves + 1

                    if userPasscode[4] == passcode[4]:
                        print("you got the 5th one right")

                        userInput6 = input("You are in the magic maze level 6. Which way do you want to go? ")
                        userPasscode = userPasscode + userInput6
                        moves = moves + 1

                        if userPasscode[5] == passcode[5]:
                            won = True
                            print("YOU WON THE GAME")
                            print("the key was " + passcode)
                            break
                        else:
                            print("wrong")
                            userPasscode = ""
                    else:
                        print("wrong")
                        userPasscode = ""
                else:
                    print("wrong")
                    userPasscode = ""
            else:
                userPasscode = ""
                print("wrong")
        else:
            print("wrong")
            userPasscode = ""

    else:
        print("wrong")
        userPasscode = ""

if won == False:
    print("you lost")
