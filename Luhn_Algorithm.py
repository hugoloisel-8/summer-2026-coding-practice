def verify_card_number(card_number):
    # Luhn algorithm validation of a credit card number

    sum_of_odd_digits = 0

    # Reverse the card number to process digits from right to left
    card_number_reversed = card_number[::-1]

    # Extract digits in odd positions (based on reversed string)
    odd_digits = card_number_reversed[::2]

    # Sum all odd-position digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0

    # Extract digits in even positions (based on reversed string)
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        # Double each even-position digit
        number = int(digit) * 2

        # If result is two digits, add them together (e.g. 12 → 1 + 2 = 3)
        if number >= 10:
            number = (number // 10) + (number % 10)

        sum_of_even_digits += number

    # Total sum of processed digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Valid if total is divisible by 10
    return total % 10 == 0


def main():
    # Example card number with separators
    card_number = '4111-1111-4555-1142'

    # Remove hyphens and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Validate the card number using Luhn algorithm
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
main()
