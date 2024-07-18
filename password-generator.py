# Importing the random module
import random

# Define the characters that can be used in the password
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+=-'

# Ask the user for the number of passwords to generate
number = int(input('Number of passwords: '))

# Ask the user for the length of each password
length = int(input('Password length: '))

# Loop to generate the required number of passwords
for _ in range(number):
    password = ''
    for _ in range(length):
        # Add a random character to the password
        password += random.choice(chars)
    # Print the generated password
    print(f'Your password: {password}')
