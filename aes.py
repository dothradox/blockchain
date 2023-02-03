from Crypto.Cipher import AES
import random
import secrets

def padding(message):
    while len(message)%16 != 0:
        message = message + " "
    
    # Return in byte form
    return message.encode()

def encrypt_aes(message,key,mode,IV):

    encryption_cipher = AES.new(key,mode,IV.encode())

    # We can finally encrypt the message using the cipher 
    encrypted_message = encryption_cipher.encrypt(message)
    print(f"This is the encrypted form: \n {encrypted_message}")

    #Since decrypt() cannot be called after encrypt(), create a new cipher with the same configuration

    decryption_cipher = AES.new(key,mode,IV.encode())
    decrypted_message = decryption_cipher.decrypt(encrypted_message)
    print(f"This is the original message: \n {(decrypted_message.decode().strip())}")

    return decrypted_message


if __name__ == "__main__":
    message = "This is a confidential information"
    padded_message = padding(message)
    
    # Use the secrets package for keys
    key= secrets.token_hex(16).encode()

    # os.urandom can also be used to generate random numbers
    # os.urandom is still pseudo-random, but cryptographically secure pseudo-random, which makes it much  more suitable for a wide range of use cases compared to random.

    # Cipher BlockChain mode 
    mode = AES.MODE_CBC

    # Set Initialization Vector to 16 bytes
    IV = ''.join(random.choice('0123456789ABCDEF') for i in range(16))

    encrypt_aes(padded_message,key,mode,IV)

