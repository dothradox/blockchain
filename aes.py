from Crypto.Cipher import AES
import hashlib


def padding(message):
    while len(message)%16 != 0:
        message = message + " "
    
    # Return in byte form
    return message.encode()

password = "Th1$1$@$trongP@$$W0RD".encode()
key = hashlib.sha256(password).digest()

# Cipher BlockChain mode 
mode = AES.MODE_CBC

# Set Initialization Vector to 16 bytes
# It helps to randomize the cipher text
# Ideally it should be created randomly
IV = '16 bytes needed.'.encode()

encryption_cipher = AES.new(key,mode,IV)
decryption_cipher = AES.new(key,mode,IV)

# The input must also be in chunks of 16 bytes so padding maybe required
message = "This is a confidential information"
padded_message = padding(message)

# We can finally encrypt the message using the cipher 
encrypted_message = encryption_cipher.encrypt(padded_message)
print(f"This is the encrypted form: \n {encrypted_message}")


# We learn that decrypt() cannot be called after encrypt()
# So to display both the encrypted and decrypted message in the same terminal,
# We create a new cipher with the same key, mode, and iv.
# We decode the string and remove the padding with strip()
decrypted_message = decryption_cipher.decrypt(encrypted_message)
print(f"This is the original message: \n {(decrypted_message.decode().strip())}")

