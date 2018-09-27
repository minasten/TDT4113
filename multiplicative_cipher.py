from cipher import *
from crypto_utils import modular_inverse
import random

class Multiplicative(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()


    def encode(self, message, key):
        encrypted = ''
        for char in message:
            char_to_number = ((ord(char) - 32) * key) % 95
            encrypted += Cipher().dictionary[char_to_number]
        print('Sender is encrypting multiplicative cipher')
        #print(encrypted)
        return encrypted

    def decode(self, message, key):
        decrypted = ''
        decrypt_key = modular_inverse(key, 95)
        #print('Using multiplicative decryption key: ',decrypt_key)
        for char in message:
            char_to_number = ((ord(char) - 32) * decrypt_key) % 95
            decrypted += Cipher().dictionary[char_to_number]
        print('Receiver is decrypting multiplicative cipher')
        #print(decrypted)
        return decrypted


    def generate_keys(self):
        n = random.randint(0,10)
        while True:
            if not modular_inverse(n, 95):
                n = random.randint(0,10)
            else:
                return n


    def possible_keys(self):
        possible = []
        for x in range(0, 10):
            possible.append(x)
        print('Possible keys for multiplicative cipher: ', possible)
        return possible

    def __str__(self):
        return 'Multiplicative'