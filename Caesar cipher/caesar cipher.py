from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, d_direction):
  cipher_text = ""
  if direction == "decode":
    shift_amount *= -1 
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    else:
      cipher_text += letter 
  print(f"The {d_direction}d text is {cipher_text}")

should_continue = True
while should_continue:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(plain_text=text, shift_amount=shift, d_direction=direction)

  question = input("Type 'yes' if you want to go again, otherwise type 'no'\n")
  if question == "no":
    should_continue = False
    print("Goodbye")


