import hashlib

def add_user(username, real_name, password):
    with open("passwd.txt", "a") as file:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        file.write(f"{username}:{real_name}:{hashed_password}\n")
    print("User Created.")

def main():
    print("Enter new user details:")
    username = input("Enter new username: ").strip()
    real_name = input("Enter real name: ").strip()
    password = input("Enter password: ").strip()

    with open("passwd.txt", "r") as file:
        existing_usernames = [line.split(":")[0] for line in file.readlines()]

    if username in existing_usernames:
        print("Cannot add. Most likely username already exists.")
    else:
        add_user(username, real_name, password)

if __name__ == "__main__":
    main()

def del_user(username):
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    with open("passwd.txt", "w") as file:
        user_deleted = False
        for line in lines:
            if line.startswith(username + ":"):
                print("User Deleted.")
                user_deleted = True
            else:
                file.write(line)

        if not user_deleted:
            print("User not found. Nothing changed.")

def main():
    username = input("Enter username: ").strip()
    del_user(username)

if __name__ == "__main__":
    main()

import hashlib

def change_password(username, current_password, new_password):
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    with open("passwd.txt", "w") as file:
        password_changed = False
        for line in lines:
            parts = line.split(":")
            if parts[0] == username and hashlib.md5(current_password.encode()).hexdigest() == parts[2]:
                hashed_new_password = hashlib.md5(new_password.encode()).hexdigest()
                file.write(f"{username}:{parts[1]}:{hashed_new_password}\n")
                print("Password changed.")
                password_changed = True
            else:
                file.write(line)

        if not password_changed:
            print("Invalid current password or user not found. Nothing changed.")

def main():
    username = input("User:             ").strip()
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")

    if new_password != confirm_password:
        print("Passwords do not match. Nothing changed.")
    else:
        change_password(username, current_password, new_password)

if __name__ == "__main__":
    main()

import hashlib

def login(username, password):
    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0] == username and hashlib.md5(password.encode()).hexdigest() == parts[2]:
                return True
    return False

def main():
    username = input("User:     ").strip()
    password = input("Password: ")

    if login(username, password):
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()