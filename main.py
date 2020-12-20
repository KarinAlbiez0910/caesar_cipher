
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  message = ''

  for letter in text:
    if not letter.isalpha():
      shift_letter = letter
    else:
      letter_index = alphabet.index(letter)
      if direction == 'encode': 
        letter_index_with_shift = letter_index + shift
      if direction == 'decode':
        letter_index_with_shift = letter_index - shift
      try:
        shift_letter = alphabet[letter_index_with_shift]
      except IndexError:
        new_index = letter_index_with_shift % 26
        shift_letter = alphabet[new_index]

    message = message + shift_letter
  print(f'The {direction}d text is "{message}".') 

game_is_active = True

while game_is_active:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)
  repeat = input('Do you want to restart the cipher game?\nType "yes" if you want to go again. Otherwise type "no".')
  if repeat == 'no':
    game_is_active = False
    print('Goodbye.')







