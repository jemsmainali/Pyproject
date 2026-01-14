import random
import string


def generate_password(min_length, use_numbers=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if use_numbers:
        characters += digits
    if use_special:
        characters += special

    pwd = ""
    has_number = False
    has_special = False

    while len(pwd) < min_length or (use_numbers and not has_number) or (use_special and not has_special):
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

    return pwd

min_length = int(input("Enter the minimum length: "))
use_numbers = input("Do you want numbers? (y/n): ").lower() == 'y'
use_special = input("Do you want special characters? (y/n): ").lower() == 'y'

password = generate_password(min_length, use_numbers, use_special)
print("Generated Password:", password)
