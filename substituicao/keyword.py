

def newAlphabet(keyWord, alphabet):
    newAlphabet = ''

    for char in alphabet:
        if char not in keyWord.lower(): 
            newAlphabet += char 

    return keyWord+newAlphabet


def encode(keyWord, msg):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    alpha = newAlphabet(keyWord, ALPHABET)
    
    new_msg = ''

    for char in msg.lower():
        if not char.isalpha():
            new_msg += char 
        else:
            index = ALPHABET.find(char)    
            new_msg += alpha[index]

    return new_msg


def cifra(keyWord, msg):
    return encode(keyWord, msg)

def main():
    print(cifra("marvin", "Arthur Dent"))
    
    
if __name__ == "__main__":
    main()