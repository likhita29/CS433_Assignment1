#These functions are used in client.py and server.py to encrypt and transpose text

def substitute(text, s): 
    text = text.strip()
    result = "" 
    for i in range(len(text)): 
        char = text[i]
        # print(char)
        if (char.isnumeric()):
            temp = ord(str((int(char)+s)%10))
            result += chr(temp)
        elif (char.isupper()): 
            temp = (ord(char) + s-65) % 26 + 65
            result += chr((ord(char) + s-65) % 26 + 65) 
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result 

def transpose(text):
    new_cmd = ""
    for word in text.split():
        rev_word = word[::-1]
        new_cmd += rev_word
        new_cmd += " "
    return new_cmd