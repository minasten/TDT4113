from affine_cipher import *
from caesar_cipher import *
from multiplicative_cipher import *
from unbreakable_cipher import *
from sender_person import *
from receiver_person import *
from hacker import *


def main():

    #s = Sender()
    r = Receiver()

    message = input('Type in message to send: ')
    cipher = choose_cipher()

    s = Sender(cipher)
    #r = Receiver(cipher)

    encoded_message = s.operate_cipher(message)
    print("Encoded message in main", encoded_message)

    print(s.get_key())
    Hacker().super_hack(encoded_message, cipher)


    decoded_message = r.operate_cipher(encoded_message, s)
    print('Decoded message in main', decoded_message)



def choose_cipher():
    print("**************************************************************************")
    print('CHOOSE CIPHER')
    print("1: Caesar\t\t2: Multiplicative\t\t3: Affine\t\t4: Unbreakable")
    print("**************************************************************************")
    c = str(input(">> "))
    while c.lower() not in ('1', '2', '3', '4', '5', 'c', 'm', 'a', 'u', 'cipher',
                            'multiplicative', 'affine', 'unbreakable'):
        print('Try again...')
        c = str(input(">> "))
    if c == '1' or c.lower() == 'cipher' or c.lower() == 'c':
        return Caesar()
    elif c == '2' or c.lower() == 'multiplicative' or c.lower() == 'm':
        return Multiplicative()
    elif c == '3' or c.lower() == 'affine' or c.lower() == 'a':
        return Affine()
    elif c == '4' or c.lower() == 'unbreakable' or c.lower() == 'u':
        return Unbreakable()


main()
