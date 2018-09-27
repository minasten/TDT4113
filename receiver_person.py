from person import *
from caesar_cipher import *
from multiplicative_cipher import *
from affine_cipher import *
from unbreakable_cipher import *
from sender_person import *

class Receiver(Person):

    def __init__(self):
        super(Person, self).__init__()


    def set_key(self, s):
        self.key = s.get_key()

    def get_key(self):
        return self.key

    def operate_cipher(self, message, s):
        if s.get_cipher().__str__() == "Affine":
            key_1, key_2 = s.get_key()
            print('Sender used keys: ', key_1, key_2)
            return s.get_cipher().decode(message, key_1, key_2)

        else:
            key = s.get_key()
            print('Sender used key: ', key)
            return s.get_cipher().decode(message, key)
             
