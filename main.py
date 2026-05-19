usernames_passwords = {"que": "qwerty123", "Therh": "forget123"}

username = input("Input username or email")
password = input("Input password")

if username in usernames_passwords:
    if password == usernames_passwords[username]:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("username invalid")

