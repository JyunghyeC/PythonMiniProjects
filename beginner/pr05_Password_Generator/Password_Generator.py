import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
lst_pw = []

print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(1, num_letters + 1):
    lst_pw.append(random.choice(letters))

for i in range(1, num_symbols + 1):
    lst_pw.append(random.choice(symbols))

for i in range(1, num_numbers + 1):
    lst_pw.append(random.choice(numbers))

# Change the order of the numbers, letters, and symbols
random.shuffle(lst_pw)

for i in lst_pw:
    password += i

print("Your password : " + password)

