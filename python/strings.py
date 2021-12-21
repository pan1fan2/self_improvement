my_string = """hello\
    world
"""

#string is immutable
#my_string[0] = 'H'

my_string = '   Hello   World   '
my_string = my_string.strip()
my_string = ' '.join(my_string.split())
print(my_string)
print(my_string.find('o'))
print(my_string.count('p'))
