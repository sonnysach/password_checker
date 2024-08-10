import sys


password = input("Please enter your password: ")
attempt = 1
while password != 'opensesame':
    if attempt > 3:
        sys.exit("Too many incorrect attempts.")
    password = input("Incorrect! Please try again: ")
    attempt += 1
print("Welcome!")


