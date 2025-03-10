import string

def caesar_cipher():
    while True:
        alphabet = string.ascii_lowercase
        result = ""
        mode = input("Encrypt or decrypt? (type [1]Encrypt, [2]Decrypt, or 'exit' to quit): ")
    
        if mode.lower() == "exit":
            print("Goodbye!")
            return        
    
        text = input("Enter text: ")
        shift = int(input("Shift value: "))

        for char in text:
            if char.isalpha():
                base = string.ascii_uppercase if char.isupper() else alphabet
                index = base.index(char.lower())
                if mode == "1" or mode.lower() == "encrypt":
                    new_index = (index + shift) % 26
                elif mode == "2" or mode.lower() == "decrypt":
                    new_index = (index - shift) % 26

                else:
                    print("Invalid mode! Try again.")
                    return
                
                result += base[new_index].upper() if char.isupper() else base[new_index]
            else:
                result += char
        action = "Encrypted" if mode == "1" else "Decrypted"
        print(f"{action} message: {result}")

caesar_cipher()