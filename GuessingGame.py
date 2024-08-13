import random as rs


IfCorrect = False

while IfCorrect == False:

    NoOfGuessLeft = 3 

    Level = input("enter the difficulty level,[Easy[E],Medium[M],Hard[H]]: ")
    while NoOfGuessLeft > 0:
        if Level == "E":
            ActualGuess = rs.randint(1,10)
            print("THE NUMBER IS BETWEEN 1 AND 10!")
            print(ActualGuess)
            Guess = int(input("Enter Guess: "))
            if Guess == ActualGuess:
                print("You win")
                IfCorrect = True
                NoOfGuessLeft = 0
            else:
                print("You Lose!,Try again")
                NoOfGuessLeft = NoOfGuessLeft - 1

        elif Level == "M":
            ActualGuess = rs.randint(1,50)
            print("THE NUMBER IS BETWEEN 1 AND 50!")
            Guess = int(input("Enter Guess: "))
            if Guess == ActualGuess:
                print("You win")
                IfCorrect = True
                NoOfGuessLeft = 0
            else:
                print("You Lose!,Try again")
                NoOfGuessLeft = NoOfGuessLeft - 1

        elif Level == "H":
            ActualGuess = rs.randint(1,100)
            print("THE NUMBER IS BETWEEN 1 AND 100!")
            Guess = int(input("Enter Guess: "))
            if Guess == ActualGuess:
                print("You win")
                IfCorrect = True
                NoOfGuessLeft = 0
            else:
                print("You Lose!,Try again")
                NoOfGuessLeft = NoOfGuessLeft - 1
                
    if NoOfGuessLeft == 0:
        ye_no = input("Do you want to try again? [Y/N]: ")
        if ye_no == "N":
            IfCorrect = True
        else:
            None

    