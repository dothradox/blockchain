import unittest
from aes import padding, encrypt_aes
from Crypto.Cipher import AES
import random
import secrets

class TestAES(unittest.TestCase):

    def test_padding(self):
        message = "Change this into 16 byte chunks"
        self.assertEqual(len(padding(message))%16, 0)

    def test_encryption(self):
        message = "Confidential, DO NOT OPEN"
        padded_message = padding(message)
        key= secrets.token_hex(16).encode()
        mode = AES.MODE_CBC
        IV = ''.join(random.choice('0123456789ABCDEF') for i in range(16))

        self.assertEqual(encrypt_aes(padded_message,key,mode,IV), padded_message)


if __name__ == '__main__':
    unittest.main()