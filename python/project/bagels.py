import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    while True:
        secretNum = getSecretNum()
        guess = ''
        print("""
            I have thought up a number.
            you have {} guesses to get it.
        """.format(MAX_GUESSES))
        numGuess = 1
        while numGuess <= numGuess:
            guess = ''
            # looping until a valid entry
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuess))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuess += 1
            if guess == secretNum:
                break
            if numGuess > MAX_GUESSES:
                print("""
                    You ran out of guesses.
                    The answer was {}.
                """.format(secretNum))
        # Ask whether to play one more round?
        print('Do you want to play again?')
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing")
            

def getSecretNum():
    """
    Returns a string made up of NUM_DIGITS unique random digits.
    """
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:NUM_DIGITS])

def getClues(guess,secretNum):
    """
    Returns a string with the pico, fermi, bagels clues for a guess and 
    secret number pair
    """
    if guess == secretNum:
        return 'Congratulations'
    
    clues = []

    for i in range(len(guess)) :
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        # Sort the clues alphabetically so the original order 
        # does not give away information
        clues.sort()
        return ''.join(clues)

if __name__ == '__main__':
    main()
        

