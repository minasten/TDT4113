from cipher import *
import random
from time import sleep

class Caesar(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()



    def encode(self, message, key):
        encrypted = ''
        for char in message:
            char_to_number = (ord(char) + key - 32) % 95                #-32 siden dictionary starter på 0 og ikke 32
            encrypted += Cipher().dictionary[char_to_number]
        print('Sender is encrypting caesar cipher')
        #print(encrypted)
        return encrypted


    def decode(self, message, key):
        decrypted = ''
        for char in message:
            char_to_number = (ord(char) - key - 32) % 95
            decrypted += Cipher.dictionary[char_to_number]
        print('Receiver is decrypting caesar cipher')
        #print(decrypted)
        return decrypted


    def generate_keys(self):
        return random.randint(0, 10)

    def possible_keys(self):
        possible = []
        for x in range(0,10):
            possible.append(x)
        print('Possible keys for caesar cipher: ', possible)
        return possible


    def __str__(self):
        return 'Ceasar'


