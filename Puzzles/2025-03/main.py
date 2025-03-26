import string
import math

def base3_to_ascii(base3_string):
  """Converts a base-3 string to its ASCII equivalent."""

  decimal_value = 0
  for digit in base3_string:
    if digit not in '012':
      raise ValueError("Invalid base-3 character: {}".format(digit))
    decimal_value = decimal_value * 3 + int(digit)

  if decimal_value > 127:  # Limit to ASCII range
      raise ValueError("Decimal value out of ASCII range: {}".format(decimal_value))
  return chr(decimal_value)

def caesar_decoder(ciphertext, shift):
    """
    Decodes a Caesar cipher.

    Args:
        ciphertext: The encrypted text.
        shift: The integer shift value used for encryption.

    Returns:
        The decrypted plaintext.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
        elif char.isdigit():
             shifted_char = str((int(char) - shift) % 10)
        else:
            shifted_char = char
        plaintext += shifted_char
    return plaintext

   
def ascii_to_base3(text):
    base3_string = ""
    for char in text:
        ascii_val = ord(char)
        base3_val = convert_to_base(ascii_val, 3)
        
        base3_string += " "+base3_val.zfill(5) # Ensure each char's base 3 is 5 digits
    return base3_string

def convert_to_base(n, base):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, base)
        nums.append(str(r))
    return ''.join(reversed(nums)) 

def base3_to_txt(file):
    words = file.read().replace("\n","").split(" ")
    output =  ""
    print(words)
    for word in words:
        try:
            output+=base3_to_ascii(word)
        except ValueError:
           print(f"Cant Convert {word}")
    
    return output

with open("input.txt",mode="r") as file:
    nextClue = base3_to_txt(file)
    nextClue=nextClue.split("!")
    nextClue=nextClue[1].split()
    nextClue=nextClue[0]
    
    pi = math.pi
    base3= ascii_to_base3(nextClue).split(" ")
    base3.remove("")
    print(base3)
    output=[]
    for num in base3:
        num=int(num,3)
        num/=pi
        output.append(num)
    text_output=""
    for num in output:
        text_output+=chr(int(num))
    print(text_output)