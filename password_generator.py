# Easy level password generator
import random
password = ""
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '*', '/']
print("Welcome to password generator")
number_of_letter = int(input("Number of letter: \n"))
number_of_number = int(input("Number of number: \n"))
number_of_symbol = int(input("Number of symbol: \n"))
for x in range(number_of_letter):
  password += random.choice(letters)
for x in range(number_of_number):
  password += random.choice(numbers)
for x in range(number_of_symbol):
  password += random.choice(symbols)
print(password)


# Hard level password generator
import random
password = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '*', '/']
print("Welcome to password generator")
number_of_letter = int(input("Number of letter: \n"))
number_of_number = int(input("Number of number: \n"))
number_of_symbol = int(input("Number of symbol: \n"))
for x in range(number_of_letter):
  password.append(random.choice(letters))
for x in range(number_of_number):
  password.append(random.choice(numbers))
for x in range(number_of_symbol):
  password.append(random.choice(symbols))
print(password)
random.shuffle(password)
print("".join(password))



# Hard level password generator using function
import random

def genPass(i, j, k):
  password = []
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '*', '/']
  for x in range(i):
    password.append(random.choice(letters))
  for x in range(j):
    password.append(random.choice(numbers))
  for x in range(k):
    password.append(random.choice(symbols))
  random.shuffle(password)
  print("".join(password))

print("Welcome to password generator")
number_of_letter = int(input("Number of letter: \n"))
number_of_number = int(input("Number of number: \n"))
number_of_symbol = int(input("Number of symbol: \n"))
genPass(number_of_letter, number_of_number, number_of_symbol)
