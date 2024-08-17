import json

def sign_up():
    print("Sign Up")
    username = input("Enter username: ")
    password = input("Enter password: ")
    mobile_no = input("Enter mobile number: ")

    user_data = {
        "username": username,
        "password": password,
        "mobile_no": mobile_no
    }

    try:
        with open("user_database.json", "r") as f:
            database = json.load(f)
    except FileNotFoundError:
        database = []

    database.append(user_data)

    with open("user_database.json", "w") as f:
        json.dump(database, f, indent=4)

    print("Sign up successful!")

def sign_in():
    print("Sign In")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("user_database.json", "r") as f:
            database = json.load(f)
    except FileNotFoundError:
        print("No user database found. Please try to sign up first.")
        return
    
    for user in database:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome to the device! Your mobile number is {user['mobile_no']}")
            return
    
    print("Incorrect credentials. Terminating the program.")

def main():
    while True:
        print("1. Sign Up")
        print("2. Sign In")
        choice = input("Enter your choice: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

