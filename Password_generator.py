import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Generate a secure random password that satisfies given constraints

    # Define character pools
    letters = string.ascii_letters      # a-z + A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # special characters

    # Combine all allowed characters into one pool
    all_characters = letters + digits + symbols

    while True:
        password = ''

        # Build a random password of the desired length
        for _ in range(length):
            password += secrets.choice(all_characters)

        # Define constraints using regex patterns
        constraints = [
            (nums, r'\d'),                 # number of digits required
            (special_chars, fr'[{symbols}]'),  # number of special characters required
            (uppercase, r'[A-Z]'),        # number of uppercase letters required
            (lowercase, r'[a-z]')         # number of lowercase letters required
        ]

        # Check if password meets all constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


if __name__ == '__main__':
    # Generate and display a new secure password
    new_password = generate_password()
    print('Generated password:', new_password)
