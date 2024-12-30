import string
import random
def generate_key():
    """Generate encryption and decryption keys."""
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    shuffled = ''.join(random.sample(characters, len(characters)))
    encrypt_key = dict(zip(characters, shuffled))
    decrypt_key = dict(zip(shuffled, characters))
    return encrypt_key, decrypt_key

def encrypt(text, key):
    """Encrypt the given text using the substitution key."""
    return ''.join(key.get(char, char) for char in text)

def decrypt(text, key):
    """Decrypt the given text using the substitution key."""
    return ''.join(key.get(char, char) for char in text)

if __name__ == "__main__":
    # Generate keys
    encrypt_key, decrypt_key = generate_key()

    # Input message
    message = input("Enter the message to encrypt: ")

    # Encryption
    encrypted_message = encrypt(message, encrypt_key)
    print("Encrypted Message:", encrypted_message)

    # Decryption
    decrypted_message = decrypt(encrypted_message, decrypt_key)
    print("Decrypted Message:", decrypted_message)
