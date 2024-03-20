alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shif_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shif_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shif_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Your {cipher_direction}d text is: {end_text}")


import art

print(art.logo)

game_is_done = False
while not game_is_done:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    restart = input("Want to try again? Type 'yes' or 'no':\n ").lower()
    if restart == "no \n":
        game_is_done = True
        print("Goodbye")
