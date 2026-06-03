def convert_to_snake_case(pascal_or_camel_cased_string):
    # Convert a PascalCase or camelCase string into snake_case

    snake_cased_char_list = [
        # If the character is uppercase, prepend an underscore and convert it to lowercase
        '_' + char.lower() if char.isupper()
        
        # Otherwise keep the character as it is
        else char
        
        # Loop through each character in the input string
        for char in pascal_or_camel_cased_string
    ]

    # Join the list into a single string and remove leading underscore if present
    return ''.join(snake_cased_char_list).strip('_')


def main():
    # Example usage of the conversion function
    print(convert_to_snake_case('BonjourJeSuisHugoLoisel'))


# Run the program
main()
