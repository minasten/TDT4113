from person import *
from caesar_cipher import *
from multiplicative_cipher import *
from affine_cipher import *
from unbreakable_cipher import *

class Sender(Person):

    def __init__(self, cipher):
        super(Person, self).__init__()
        self.cipher = cipher



    def set_key(self, key_word):
        if self.cipher.__str__() == 'Unbreakable':
            self.key = self.cipher.generate_keys(key_word)
        else: 
            self.key = self.cipher.generate_keys()
        


    def get_key(self):
        return self.key

    def get_cipher(self):
        return self.cipher


    def operate_cipher(self, message):
        if self.cipher.__str__() == 'Affine':
            self.set_key("")
            key_1, key_2 = self.get_key()
            print('Using keys: ', key_1, key_2)
            encoded_message = self.cipher.encode(message, key_1, key_2)
            return encoded_message

        elif self.cipher.__str__() == 'Unbreakable':
            self.set_key(self.cipher.check_keyword())
            key_word_as_list = self.get_key()
            print('Using as key: ', key_word_as_list)
            encoded_message = self.cipher.encode(message, key_word_as_list)
            return encoded_message

        else:
            self.set_key("")
            print('Using key: ', self.get_key())
            encoded_message = self.cipher.encode(message, self.get_key())
            return encoded_message

        print('Encoded message: ', encoded_message)


