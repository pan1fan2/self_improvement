import datetime, random

def getBirthdays(numberofBirthdays):
    """Returns a list of number random state objects for birthdays

    Args:
        numberofBirthdays ([int]): Number of birthdays
    """
    birthdays = []
    for i in range(numberofBirthdays):
        startOfYear = datetime.date(2020, 1, 1)
        randNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns of the date object of a birthday that occurs more than once

    Args:
        birthdays ([list]): list of birthdays
    """
    if len(birthdays) == len(set(birthdays)):
        return None   # all unique , return none
    
    for a , birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA

# Set up a tuple of month name in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:
    print('How many birthdays shall I generate?')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0 :
        print(', ', end = '')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName,birthday.day)
    print(dateText, end = '')
    
print()
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end = '')

if match != None:
    monthName = MONTHS[match.month - 1]
    dataText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times.')
print('Press Enter to start.')

simMatch = 0    #How many simulations had matching birthdays in them.
for i in range(100000):
    if i % 10000 == 0 :
        print(i, 'simulation run..')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print('100,000 simulations run.')

probability = round(simMatch / 100000 * 100 ,2)
print(f"""
    Out of 100,000 simulations of {numBDays} people, there was a matching 
    birthdays in that group, {simMatch} times. This means that {numBDays} people 
    have a {probability} % chance of having a matching birthday in their group.
    That's probably more than you would think.
""")
