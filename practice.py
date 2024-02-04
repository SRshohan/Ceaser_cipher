all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


key = "ORANGE"
key_dict = {}

for i in range(len(key)):
    part = all_letters.find(key[i])

    fst_part = all_letters[:part]
    lst_part = all_letters[part:]
    new_letters = lst_part + fst_part  # Concatonate two string
    # print(f"First part of the letters {fst_part} and last part of the letters {lst_part} and combined {new_letters}")

    key_dict[key[i]] = new_letters

# print(key_dict)

cipherT = []
inpt = "THEQUICKBROWNFOX"


def encription(key, inpt):
        for num, char in enumerate(inpt):
                if char in all_letters:
                        key_char = key [num % len(key)]
                        cipher_index = all_letters.find(char)
        # print(cipher_index)
                        cipher_char = key_dict[key_char][cipher_index]
                        cipherT.append(cipher_char)

        cipherText = "".join(cipherT)
        return cipherText





def decription( key, cipherText):
        decreption = []
        for num, char in enumerate(cipherText):
                if char in all_letters:
                        decrept_key = key[num % len(key)]
                        decrept_index = key_dict[decrept_key].find(char)
                        decrept_char = all_letters[decrept_index]
                        decreption.append(decrept_char)

        decrept = "".join(decreption)
        return decrept

answer = input("Enter 'e' for encription and 'd' for decreption: ")

if answer.lower() == "e":
       print(encription(key, inpt))
elif answer.lower() == "d":
       input_cipher_for_plain = input("Enter ciphertext to decrypt: ")
       cipherText= input_cipher_for_plain.upper()
       print(decription(key, cipherText))
