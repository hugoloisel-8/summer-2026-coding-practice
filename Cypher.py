text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'


def vigenere(message, key, direction=1):
    # Main Vigenère cipher function used for both encryption and decryption
    # direction = 1 → encrypt
    # direction = -1 → decrypt

    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    # Loop through each character in the message
    for char in message.lower():

        # If the character is not a letter, keep it unchanged
        if not char.isalpha():
            final_message += char
        else:        
            # Select the corresponding character from the key (cycling through it)
            key_char = key[key_index % len(key)]
            key_index += 1

            # Get the shift value based on the key character
            offset = alphabet.index(key_char)

            # Find the position of the current character in the alphabet
            index = alphabet.find(char)

            # Apply the shift depending on encryption or decryption
            new_index = (index + offset * direction) % len(alphabet)

            # Append the transformed character to the final message
            final_message += alphabet[new_index]
    
    return final_message


def encrypt(message, key):
    # Encrypt message using Vigenère cipher
    return vigenere(message, key)


def decrypt(message, key):
    # Decrypt message using Vigenère cipher (reverse direction)
    return vigenere(message, key, -1)


# Display original encrypted text and key
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Decrypt the message
decryption = decrypt(text, custom_key)

# Display decrypted result
print(f'\nDecrypted text: {decryption}\n')
