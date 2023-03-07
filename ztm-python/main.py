# # Section 2.9
print('dec0de284')
name = input('What is your name?\nName: ')
print('Hello, ' + name + '!')

# # Section 3.21
# # int and float
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))
print(type(0))
print(type(18 + 2.0))
print(2 ** 2)
print(5 // 2)  # rounded division
print(6 % 4)

# # Section 3.22
# # Math Functions
print(round(2.5))
print(abs(-3.5))

# # Section 3.24
# # Operator Precedence
# # Order:
# # ()
# # **
# # * /
# # + -

# # Section 3.26
print(bin(5))
print(int('0b101', 2))

# # Section 3.27
iq = 190
print(iq)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# # Section 3.29
# # Augmented Assignment Operator
a = 1
a += 1
print(a)

# # Section 3.30
long_string = '''Hello, there!
I'm dec0de284.
Nice to meet you!
'''
print(long_string)

# # Section 3.32
print('Hello! I\'m dec0de' + str(284))

# # Section 3.34
name = 'dec0de284'
programming_language = 'Python'
print(f'Hi! I\'m {name}, and I\'m currently studying {programming_language}!')
print('Hi! I\'m {1}, and I\'m currently studying {0}!'.format(programming_language, name))

# # Section 3.35
name = 'dec0de284'
# [start:stop:step-over]
# Reversed Order
print(name[::-1])

# # Section 3.39
try:
    yourFavNumber = int(input("What is your favorite number?\nAnswer: "))
    myFavNumber = 284
    if yourFavNumber > myFavNumber:
        print(f"Your favorite number '{yourFavNumber}' is larger than my favorite number '{myFavNumber}'.")
    else:
        print(f"Your favorite number '{yourFavNumber}' is less than my favorite number '{myFavNumber}'.")
except Exception as e:
    print(e)

# # Section 3.41
try:
    name = input("What is your name?\nName: ")
    favColor = input("What is your favorite color?\nAnswer: ")
    characterLength = len(favColor)
    print(f"{name}, your favorite color has {characterLength} characters. When hidden, it's {'*' * characterLength}.")
except Exception as e:
    print(e)

# # Section 3.43
favColors = ['Purple', 'White', 'Pink']
newFavColors = favColors[:]
newFavColors[1] = 'Black'
print(favColors)
print(newFavColors)

# # Section 3.55
player = {
    'weapon': 'UMP9',
    'name': 'dec0de284',
    'health': 284
}
print(f"{player['name']}'s weapon is a {player['weapon']} and have a HP of {player['health']}.")
print(f"Does {player['name']} have an armor? {'armor' in player}")

# # Section 4.64
# # Ternary Operator
isFriend = True
canMessage = "message allowed" if isFriend else "denied message"
print(canMessage)


# # Section 4.64
# # Functions
def sample_function():
    print("This is a sample Function.")


print(f"The sample_functions is located at: {sample_function}")


# # Section 4.86
# # Docstrings
def test_function(a):
    """
    This function prints a
    """
    print(a)


test_function('sample')
