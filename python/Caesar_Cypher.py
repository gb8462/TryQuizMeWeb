import string

def caesar_cipher():
    while True:
        alphabet = string.ascii_lowercase
        result = ""
        mode = input("Encrypt or decrypt? (type [1]Encrypt, [2]Decrypt, or 'exit' to quit): ").strip().lower()

        if mode == "exit":
            print("Goodbye!")
            return        

        if mode not in ["1", "2", "encrypt", "decrypt"]:
            print("Invalid mode! Try again.")
            continue  # Restart the loop
    
        text = input("Enter text: ")
        try:
            shift = int(input("Shift value: "))
        except ValueError:
            print("Invalid shift value! Enter a number.")
            continue

        for char in text:
            if char.isalpha():
                base = string.ascii_uppercase if char.isupper() else alphabet
                index = base.index(char)
                new_index = (index + shift) % 26 if mode in ["1", "encrypt"] else (index - shift) % 26
                result += base[new_index]
            else:
                result += char
        
        action = "Encrypted" if mode in ["1", "encrypt"] else "Decrypted"
        print(f"{action} message: {result}\n")

caesar_cipher()