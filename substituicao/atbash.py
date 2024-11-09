
def atbash(msg):
    Alpha = 'abcdefghijklmnopqrstuvwxyz'
    rAlpha = Alpha[::-1]

    new_msg = ''

    for char in msg.lower():

        if not char.isalpha():
            new_msg += char
        else:
            index = Alpha.find(char)
            new_msg += rAlpha[index] 
    
    return new_msg    


def main():
    msg = "may the force be with you"
    
    print(f"Mensagem: {msg}\nCriptografada: {atbash(msg)}")



if __name__ == "__main__":
    main()