from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def main():
    while 1:
        print("**********************************************")
        print("*    1. Generate Key and Encrypt Password    *")
        print("*    2. Decrypt Password                     *")
        print("*    3. Exit                                 *")
        print("**********************************************")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            password = input("Enter your password: ")
            key = generate_key()
            encrypted_password = encrypt_password(password, key)
            print(f"Generated Token (Key): {key.decode()}")
            print(f"Encrypted Password: {encrypted_password.decode()}")

        elif choice == "2":
            key = input("Enter the token (key): ").encode()
            encrypted_password = input("Enter the encrypted password: ").encode()
            try:
                decrypted_password = decrypt_password(encrypted_password, key)
                print(f"Decrypted Password: {decrypted_password}")
            except Exception as e:
                print("Failed QwQ")
                print(e)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid!")
            
        print("******************** Line ********************\n\n")

if __name__ == "__main__":
    main()