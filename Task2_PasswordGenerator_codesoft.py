import random
import string
while True:
    try:
        length = int(input("Enter the password length:"))
        if length <= 0:
            print("Invalid input.Please enter natural numbers only (positive integers).")
        else:
            break
    except ValueError:
        print("Invalid input.Please enter natural numbers only (positive numbers).")

print('''Choose character set for password length:
      1.Digits (0-9)
      2.Letters (a-z, A-Z)
      3.Special characters (!,@,#,etc.)
      4.Exit''')
characterList = ""
while True:
    choice = int(input("Pick a number from 1 to 4: "))
    if choice ==1:
        characterList += string.digits
    elif choice == 2:
        characterList += string.ascii_letters
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")
password = "".join(random.choice(characterList) for _ in range(length))
print("Your random paassword is " , password)
