import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_num, cipher_dir):
    end_text = ""
    if cipher_dir == "decode":
        shift_num *= -1
    for i in start_text:
        if i in alphabet:
            idx_1 = alphabet.index(i)
            letter = alphabet[idx_1 + shift_num]
            end_text += letter
        else:
            end_text += i
    print(f"The {cipher_dir}d text is : {end_text}")


print(art.logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_num=shift, cipher_dir=direction)

    restart = input("Do you want to run the program again? Type 'yes' or 'no'. \n")
    if restart == "no":
        should_end = True
        print("Goodbye")
