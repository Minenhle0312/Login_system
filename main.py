usernames_passwords = {"que": "qwerty123", "Therh": "forget123"}

username = input("Input username or email")
password = input("Input password")

if username in usernames_passwords:
    attempts = 0
    
    while attempts < 3
    password = input(f"Input password({3 - attempts} attempts remaining): ")
        if password == usernames_passwords[username]:
            print("Login successful")
            break
        else:
            attempts = attempts + 1
            print("Incorrect password")
            
        if attempts == 3:
            print("Max retries reached")
    else:
        print("username invalid")
   
