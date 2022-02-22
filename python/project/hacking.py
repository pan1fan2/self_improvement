import random, sys

# Set up the constants:
# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = r'~!@#$%^&*()_+-={}[]|;:,.<>?/'

with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline:
    WORDS[i] = WORDS[i].strip().upper()

def getWords():
    """Return a list of 12 words that could possibly be the password.
 
    The secret password will be the first word in the list.
    To make the game fair, we try to ensure that there are words with
    a range of matching numbers of letters as the secret word."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two more words; these have zero matching letters.
    # We use "< 3" because the secret password is already in words.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)
     
    # Find two words that have 3 matching letters (but give up at 500
    # tries if not enough can be found).
    for i in range(500):
        if len(words) == 5:
            break  # Found 5 words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).
    for i in range(500):
        if len(words) == 12:
             break  # Found 7 or more words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
             words.append(randomWord)

    # Add any random words needed to get 12 words total.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words

def getOneWordExcept(blocklist=None):
    """Returns a random word from WORDS that isn't in blocklist."""
    if blocklist == None:
         blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord

def numMatchingLetters(word1,word2):
    """Returns the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1

if __name__ == '__main__':
    #print(getOneWordExcept())
    print(getWords())
