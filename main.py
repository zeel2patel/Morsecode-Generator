MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}


def encryptor(text):
    encrypted_text = ""
    for letters in text:
        if letters != " ":
            encrypted_text = encrypted_text + MORSE_CODE_DICT.get(letters) + " "
        else:
            encrypted_text += " "
    print(encrypted_text)


def decryptor(text):
    try:
        text += " "
        key_list = list(MORSE_CODE_DICT.keys())
        val_list = list(MORSE_CODE_DICT.values())
        morse = ""
        normal = ""
        for letters in text:
            if letters != " ":
                morse += letters
                space_found = 0
            else:
                space_found += 1
                if space_found == 2:
                    normal += " "
                else:
                    normal = normal + key_list[val_list.index(morse)]
                    morse = ""
        print(normal)
    except:
        print("This Msg is not valid")


print("Morse Code Generator")

while range(10):
  ch = input("Press E To Encrypt Or D To Decrypt : ")
  if ch == 'E' or ch == 'e':
    text_to_encrypt = input("Enter Some Text To Encrypt : ").upper()
    encryptor(text_to_encrypt)
  elif ch == 'D' or ch == 'd':
    text_to_decrypt = input("Enter morse code to Decrypt : ")
    decryptor(text_to_decrypt)
    continue
  else:
    print("the end")
    break
