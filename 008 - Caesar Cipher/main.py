import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text, shift, direction):
    adjusted_string = ""
    shift = shift % len(alphabet)
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == "encode" and index + shift > len(alphabet)-1:
                adjusted_string += alphabet[(index - len(alphabet)) + shift]
            elif direction == "decode" and index - shift < 0:
                adjusted_string += alphabet[(index + len(alphabet)) - shift]
            elif direction == "encode":
                adjusted_string += alphabet[index + shift]
            elif direction == "decode":
                adjusted_string += alphabet[index - shift]          
        else:
            adjusted_string += char
    print(f"\nHere's the {direction}d result: {adjusted_string}")

run_again = "yes"

while run_again == "yes":
    os.system('clear')
    print(art.logo)
    direction = ""
    while direction not in ["encode", "decode"]:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction not in ["encode", "decode"]:
            print("Invalid entry, please try again.")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text, shift, direction)
    run_again = input("\nType 'yes' if you want to go again.  Otherwise type 'no'\n")
