#Description: This program takes an original message and returns the encrypted message following the ideas of cryptology, an ancient study of secret writing. It can also take an encrypted message and decrypt it.

import sys
import math

def pad_message(text):
    new_text = text.strip()
    L = len(new_text)
    sqrt_M = math.ceil(math.sqrt(L))
    M = sqrt_M ** 2
    num_of_stars = M - L
    padded_message = (new_text + num_of_stars*'*')
    array = [[0 for i in range(sqrt_M)] for j in range(sqrt_M)]
    for i in range(sqrt_M):
      for j in range(sqrt_M):
        array[i][j] = padded_message[i * sqrt_M + j]
    return array
        
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
    new_message = pad_message(strng)
    size = len(new_message[0])
    encrypted_message = [[0 for i in range(size)] for j in range(size)]
    encrypted_line = ''
    for i in range(size):
      for j in range(size):
        encrypted_message[j][size - 1 - i] = new_message[i][j]
    for i in range(size):
      for j in range(size):
        if encrypted_message[i][j] != '*':
          encrypted_line += encrypted_message[i][j]
    return encrypted_line
    
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    L = len(strng)
    sqrt_M = math.ceil(math.sqrt(L))
    M = sqrt_M ** 2
    num_of_stars = M - L
    padded_message = [[0 for i in range(sqrt_M)] for j in range(sqrt_M)]
    i = 0
    for column in range(sqrt_M):
      for row in reversed(range(sqrt_M)):
        if int(i) < num_of_stars:
          padded_message[row][column] = '*'
          i += 1
    c = 0
    for i in range(sqrt_M):
      for j in range(sqrt_M):
        if int(c) < L and padded_message[i][j] != '*':
          padded_message[i][j] = strng[c]
          c += 1    
    decrypted_message = [[0 for i in range(sqrt_M)] for j in range(sqrt_M)]
    decrypted_line = ''
    for i in range(sqrt_M):
      for j in range(sqrt_M):
        decrypted_message[sqrt_M - 1 - j][i] = padded_message[i][j]
    for i in range(sqrt_M):
      for j in range(sqrt_M):
        if decrypted_message[i][j] != '*':
          decrypted_line += decrypted_message[i][j]
    return decrypted_line

def main():
  # read the strings P and Q from standard input
    lines = sys.stdin.readlines()
    if len(lines) > 0:
      P = lines[0].strip()
      Q = lines[1].strip()
  # encrypt the string P
      encrypted = encrypt(P)
  # decrypt the string Q
      decrypted = decrypt(Q)
  # print the encrypted string of P
      #for k in range(len(encrypted[0])):
      print(str(encrypted))
  # and the decrypted string of Q
      #for k in range (len(decrypted[0])):
      print(str(decrypted))

if __name__ == "__main__":
    main()




