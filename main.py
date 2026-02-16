while True:
    print("\n=== Account Creation ===")

    username = input("Enter username: ")

    # Username validation loop
    while len(username) < 7:
        print("Username must be at least 7 characters.")
        username = input("Enter username again: ")

    password = input("Enter password: ")

    # Password validation loop
    while True:
        has_letter = False
        has_number = False

        if len(password) < 10:
            print("Password must be at least 10 characters.")
        else:
            for char in password:
                if char.isalpha():
                    has_letter = True
                if char.isdigit():
                    has_number = True

            if not has_letter:
                print("Password must contain at least one letter.")
            elif not has_number:
                print("Password must contain at least one number.")
            else:
                print("Account created successfully!")
                break

        password = input("Enter password again: ")

    again = input("Create another account? (yes/no): ")
    if again.lower() != "yes":
        break
