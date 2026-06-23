import time

print()
# Variables
user = "admin"
password = "secret123"
f_attempts = 0

# Programme
while True:
    # Successful Login
    login1 = input("Enter your username: ")
    login2 = input("Enter your password: ")
    if login1 == user and login2 == password:
        print()
        print(f"Welcome {login1}")
        break
    # Failed Login
    else:
        print()
        print("Wrong username or password")
        f_attempts += 1
        remaining_attempts = 3 -f_attempts
        print()
        print(f"{remaining_attempts} attempts remaining")
        if f_attempts <= 0:
            print()
            print("SERVER LOCKDOWN! - WAIT FOR 15 SECONDS")
            time.sleep(15)
            print()
            print("Restarting server.... you can try again!")

            f_attempts = 0


