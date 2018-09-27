from cipher import *
from multiplicative_cipher import *
from caesar_cipher import *


class Affine(Cipher):

    def __init__(self):
        super(Cipher, self).__init__()


    def encode(self, message, m_key, c_key):
        m_encoded = Multiplicative().encode(message, m_key)
        print('Multiplicative message to encode: ', m_encoded)
        c_encoded = Caesar().encode(m_encoded,c_key)
        print('Caeser (affine) encoded message: ', c_encoded)
        return c_encoded


    def decode(self, message, m_key, c_key):
        print('Decoding.. using multiplicative key: ', m_key, ' and caesar key: ',c_key)
        c_decoded = Caesar().decode(message, c_key)
        #print('Multiplicative message to decode: ', c_decoded)
        m_decoded = Multiplicative().decode(c_decoded, m_key)
        print('Multiplicative (affine) decoded message: ', m_decoded)
        return m_decoded


    def generate_keys(self):
        m_key = Multiplicative().generate_keys()
        print(m_key)
        c_key = Caesar().generate_keys()
        print(c_key)
        print('Multiplicative key: ', m_key, 'Caesar key: ', c_key)
        return m_key, c_key


    def possible_keys(self):
        possible_m = Multiplicative().possible_keys()
        possible_c = Caesar().possible_keys()
        return possible_m, possible_c


    def __str__(self):
        return 'Affine'