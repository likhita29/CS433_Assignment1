#These functions are used in server.py to encrypt and reverse text

def encrypt(text, s): 
    text = text.strip()
    result = "" 
    for i in range(len(text)): 
        char = text[i]
        print(char)
        if (char == " "):
            result += " "
        elif (char.isnumeric()):
            temp = ord(str((int(char)+s)%10))
            result += chr(temp)
        elif (char.isupper()): 
            temp = (ord(char) + s-65) % 26 + 65
            result += chr((ord(char) + s-65) % 26 + 65) 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result 

def reverse(text): 
    new_cmd = ""
    for word in text.split():
        rev_word = word[::-1]
        new_cmd += rev_word
        new_cmd += " "
    return new_cmd