import string
import base64
import random


def generate_password(length=12, uppercase=True, lowercase=True, digits=True, symbols=True, exclude_similar=True):
    """Creates a password from the options up here ^."""
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if exclude_similar:
        characters = characters.replace('0', '').replace('O', '').replace('1', '').replace('l', 'I')

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def encrypt_password(password):
    """Encrypts a password using base64."""
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    return encoded_password

def decrypt_password(encoded_password):
    """Decrypts a password that was encrypted by base64."""
    decoded_password = base64.b64decode(encoded_password).decode('utf-8')
    return decoded_password

def save_password(password, name):
    """Saves the encrypted password the backup."""
    encrypted_password = encrypt_password(password)
    with open('base64-backup.txtc', 'a') as f:
        f.write(f"{name}:{encrypted_password}\n")

def load_passwords():
    """Open encrypted passwords from the backup."""
    passwords = {}
    with open('j9whrh83rh9', 'r') as f:
        for line in f:
            name, encrypted_password = line.strip().split(':')
            passwords[name] = encrypted_password
    return passwords

def find_password(name):
    """Finds a password with decrypted."""
    passwords = load_passwords()
    if name in passwords:
        encrypted_password = passwords[name]
        decrypted_password = decrypt_password(encrypted_password)
        return decrypted_password
    else:
        return "Password not found."

if __name__ == "__main__":
    while True:
        print("\nPassword Creator")
        print("1. Generate a new password")
        print("2. Save a password to backup file")
        print("3. Find a password from backup file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            password = generate_password()
            print("Generated password:", password)

        elif choice == '2':
            password = input("Enter the password to save: ")
            name = input("Enter a name for the password: ")
            save_password(password, name)
            print("Password saved successfully.")

        elif choice == '3':
            name = input("Enter the name of the password to find: ")
            password = find_password(name)
            print(password)

        elif choice == '4':
            break

        else:
            print("unknown choice. Please try again.")