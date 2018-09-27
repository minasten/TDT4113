from affine_cipher import *
from caesar_cipher import *
from multiplicative_cipher import *
from unbreakable_cipher import *
from hacker import *


#TEST FOR CAESER
"""""
test_string = 'Hello, this is a secret message'

test_key = Caesar().generate_keys()

encoded = Caesar().encode(test_string, test_key)

decoded_message = Caesar().decode(encoded, test_key)

Cipher().verify(test_string, decoded_message)
"""""


#TEST FOR MULTIPLICATIVE
"""""
test_string = 'Hello, this is a secret message'

test_key = Multiplicative().generate_keys()

encoded = Multiplicative().encode(test_string, test_key)

decoded_message = Multiplicative().decode(encoded, test_key)

Cipher().verify(test_string, decoded_message)
"""""


#TEST FOR AFFINE
"""""
test_string = 'hei min elskede mina <3'

multiplicative_key, caeser_key = Affine().generate_keys()

encoded = Affine().encode(test_string, multiplicative_key, caeser_key)

decoded_message = Affine().decode(encoded, multiplicative_key, caeser_key)

Cipher().verify(test_string, decoded_message)
"""""


#TEST FOR UNBREAKABLE
"""""
test_string = 'Hello, this is a secret message'

key_word = Unbreakable().check_keyword()

key_list = Unbreakable().generate_key(key_word)

encoded = Unbreakable().encode(test_string, key_list)

decoded_message = Unbreakable().decode(encoded, key_list)

Cipher().verify(test_string, decoded_message)
"""""

"""""
sender1 = sender()
sender1.setKey()
rec1 = receiver()
rec1.setKey(sender1.getKey())
encoded = sender1.operateCipher(0)
decoded = rec1.opreateCIpher(0)
"""""

message = 'Hello this is a top secret message, do not share with anyone'

key_1, key_2 = Affine().generate_keys()

new_message = Affine().encode(message, key_1, key_2)

cipher = Affine()

Hacker().super_hack(new_message, cipher)