# imports
import random
import register
import model

global userInstance

def main():  
    userMenuInput = -1
    lowRange = 1
    highRange = 20
    numberOfGuesses = 0
    totalPossibleGuesses = 7
    wins = userInstance.wins
    losses = userInstance.losses

    print('\nWelcome to the Random Number Guessing Game!!!')
    while int(userMenuInput) != 0:
        print("******************")
        print("Welcome! Select an option")
        print("Game Menu:\n")
        print("1: Play with the range %s to %s." % (str(lowRange), str(highRange)))
        print("2: Set the range")
        print("0. Exit Game")
        print("******************")
        try:
            userMenuInput = int(input())
            if userMenuInput == 1:
                theAnswer = random.randint(lowRange, highRange)
                print("Lets Play!")
                print("Guess a number between %s and %s" % (str(lowRange), str(highRange)))
                for numberOfGuesses in range(totalPossibleGuesses):
                    try:
                        userGuessInput = int(input())
                        if userGuessInput < theAnswer:
                            print("Guess was too low!")
                            numberOfGuesses = int(numberOfGuesses + 1)
                        elif userGuessInput > theAnswer:
                            print("Guess was too high!")
                            numberOfGuesses = int(numberOfGuesses + 1)
                        elif userGuessInput == theAnswer:
                            numberOfGuesses = int(numberOfGuesses + 1)
                            userInstance.wins += 1 
                            model.session.commit()
                            wins = userInstance.wins                       
                            print("You guessed right in %s!!! The right answer was %s!!!\nwins: %s losses: %s\n" % (numberOfGuesses, theAnswer, wins, losses))
                            break
                    except ValueError:
                        print('Oops!! That is not a valid input. Please try again...')
                if numberOfGuesses == totalPossibleGuesses:
                        userInstance.losses += 1
                        model.session.commit()
                        losses = userInstance.losses
                        print("You lost.\n The answer was: %s total wins: %s total losses: %s\n" % (theAnswer, wins, losses))
                numberOfGuesses = 0
            elif userMenuInput == 2:
                try:
                    print("Set the low range.")
                    lowRange = int(input())
                    if lowRange < 0:
                        print("Please enter in a number greater than zero!")
                        print('low range is set to zero')
                        lowRange = 0
                    print("Set the high range.")
                    highRange = int(input())
                    if highRange <= lowRange:
                        print("high range can't be lower than the low range")
                        highRange = lowRange + 1000
                        print("good luck")
                    print("You have selected the range between " + str(lowRange) + " and " + str(highRange) + ".")
                except ValueError: 
                    print("Please enter a valid integer or number! Or else..")
            elif userMenuInput == 0:
                print("Goodbye!")
        except ValueError:
            print('\nOops! Please select option from the above menu.') #prints this if the input is not a number

status, userInstance = register.register()

if status == True:

    main()