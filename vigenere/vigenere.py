def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:        
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

def main():
    text = 'the cake is a lie'
    custom_key = 'portal'
    
    print(f'mensagem criptografada: {encrypt(text, custom_key)}')
    


if __name__ == "__main__":
    main()