all_letters = "ABCDEFGHIJKLMNOKPQRSTUVWXYZ"


key = "ORANGE"
key_dict = {}


    
for i in range(len(key)):
        part = all_letters.find(key[i])

        fst_part = all_letters[:part]
        lst_part = all_letters[part:]
        new_letters = lst_part + fst_part # Concatonate two string
        print(f"First part of the letters {fst_part} and last part of the letters {lst_part} and combined {new_letters}")

        key_dict[key[i]] = new_letters

        print(key_dict)

cipherT = []
inpt = "THEQUICKBROWNFOX"

for num in range(len(inpt)):
        for key, value in key_dict.items():
                cipherText = all_letters.find(inpt[num])
                cipherT.append(value[cipherText])
                
print(cipherT)
        

# index = all_letters.find(key[0])
# print(index)

# key_dict = {}
