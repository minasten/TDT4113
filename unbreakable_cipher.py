from cipher import *


class Unbreakable(Cipher):


    def __init__(self):
        super(Cipher, self).__init__()

    def encode(self, message, key_word):
        total_key_list = []
        encoded = ''
        while len(total_key_list) < len(message):
            for x in range(0, len(key_word)):
                total_key_list.append(key_word[x])
        print('List of key word numbers: ', total_key_list)
        for index in range(len(message)):
            char_to_number = ((ord(message[index]) - 32) + total_key_list[index]) % 95
            encoded += Cipher().dictionary[char_to_number]
        print('Unbreakable cipher encoded message: ', encoded)
        return encoded

    def decode(self, message, key_word):
        decoded = ''
        total_key_list = []
        while len(total_key_list) < len(message):
            for x in range(0, len(key_word)):
                total_key_list.append(key_word[x])
            #total_key_list += total_key_list
        print('List of key word numbers: ', total_key_list)
        for index in range(len(message)):
            char_to_number = ((ord(message[index]) - 32) - int(total_key_list[index])) % 95
            decoded += Cipher().dictionary[char_to_number]
        print('Unbreakable cipher decoded message: ', decoded)
        return decoded


    def check_keyword(self):
        valid = 0
        word_file = open('english_words.txt', 'r')
        key_word = input('Choose valid keyword: ')
        print('Keyword chosen: ', key_word)
        valid_words = [line.strip('\n') for line in word_file]
        word_file.close()
        while not valid:
            for line in valid_words:
                if line.strip('\n') == key_word:
                    print('Valid keyword')
                    valid = 1
                    break
            if valid == 0:
                print('Unvalid keyword, please choose a new one')
                key_word = input('Choose valid keyword: ')
                print('Keyword chosen: ', key_word)
        return key_word


    def __str__(self):
        return 'Unbreakable'


    def generate_keys(self, key_word):
        key_word_list = []
        for char in key_word:
            char_to_number = (ord(char) - 32)
            key_word_list.append(char_to_number)
        print('List of keyword: ', key_word_list)
        return key_word_list



    def possible_keys(self):
        possible_key_words = []
        word_file = open('english_words.txt', 'r')
        for line in word_file:
            temp_word = []
            for char in line.strip('\n'):
                char_to_number = (ord(char) - 32)
                temp_word.append(char_to_number)
            possible_key_words.append(temp_word)
        word_file.close()
        #print('Possible key-words: ', possible_key_words)
        return possible_key_words