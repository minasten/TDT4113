from person import *
from caesar_cipher import *
from multiplicative_cipher import *
from affine_cipher import *
from unbreakable_cipher import *

class Sender(Person):

    def __init__(self):
        super(Person, self).__init__()



    def set_key(self):
        self.key = Cipher().generate_keys()


    def get_key(self):
        return self.key


    def operate_cipher(self, message, cipher):
        self.set_key()
        if cipher.__str__() == 'Affine':
            key_1, key_2 = self.get_key()
            print('Using keys: ', key_1, key_2)
            encoded_message = cipher.encode(message, key_1, key_2)
            return encoded_message

        elif cipher.__str__() == 'Unbreakable':
            key_word = cipher.check_keyword()
            key_word_as_list = cipher.generate_keys()
            print('Using as key: ', key_word_as_list)
            encoded_message = cipher.encode(message, key_word_as_list)
            return encoded_message

        else:
            key = cipher.generate_keys()
            print('Using key: ', key)
            encoded_message = cipher.encode(message, key)

        print('Encoded message: ', encoded_message)


