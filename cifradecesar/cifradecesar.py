# Cifra de césar 

def cifradecesar(msg, direction=1):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    right = 3
    new_msg = ''

    for char in msg.lower():

        if not char.isalpha():
            new_msg += char
        else:
            index = alphabet.find(char)
            new_index = (index + right*direction) % len(alphabet)    
            new_msg += alphabet[new_index] 

    return new_msg      


def encode(msg):
    return cifradecesar(msg)

def decode(msg):
    return cifradecesar(msg, -1)


def main():
    mensagem = "hack the planet"
    encrypted = encode(mensagem)
    print(f'mensagem encriptada: {encrypted}\nmensagem solucionada: {decode(encrypted)}')
    
if __name__ == '__main__':
    main()

