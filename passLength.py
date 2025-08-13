userName = input("Enter in your username: ")
userPass = input("Enter in your password it must be more than 6 characters: ")

passLength = len(userPass)

while passLength < 6:
    userPass = input("Enter in your password it must be more than 6 characters: ")

print("Account Created!")

