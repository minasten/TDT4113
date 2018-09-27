from cipher import *


class Person(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()
        self.key = 0

    def set_key(self):
        pass

    def get_key(self):
        return self.key

    def operate_cipher(self, message, cipher):
        pass