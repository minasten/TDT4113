from person import *
import operator

class Hacker(Person):

    def __init__(self):
        super(Person, self).__init__()
        #self.wordbase = self.read_word_file()


    def super_hack(self, message, cipher):
        print(cipher)
        if cipher.__str__() == 'Unbreakable':
            possible_keys = cipher.possible_keys()
            word_file = open('english_words.txt', 'r')
            valid_words = [line.rstrip('\n') for line in word_file]
            word_file.close()
            valid_keys = {}
            for temp_key in possible_keys:
                temp_message = cipher.decode(message, temp_key)
                temp_words = temp_message.split()
                for word in temp_words:
                    if word in valid_words:
                        if '-'.join(map(str, temp_key)) in valid_keys.keys():
                            valid_keys['-'.join(map(str, temp_key))] += 1
                        else:
                            valid_keys['-'.join(map(str, temp_key))] = 1
                    if '-'.join(map(str, temp_key)) in valid_keys:
                        if valid_keys['-'.join(map(str, temp_key))] > 5:
                            most_used_key = temp_key
                            decoded_message = cipher.decode(message, most_used_key)
                            print('Hacker decoded message: ', decoded_message, '\n Using key: ', most_used_key)
                            return decoded_message


        elif cipher.__str__() == 'Affine':
            m_key, c_key = cipher.possible_keys()
            word_file = open('english_words.txt', 'r')
            valid_words = [line.rstrip('\n') for line in word_file]
            word_file.close()
            valid_m_keys = {}
            valid_c_keys = {}
            for temp_m_key in m_key:
                for temp_c_key in c_key:
                    temp_message = cipher.decode(message, temp_m_key, temp_c_key)
                    temp_words = temp_message.split()
                    #print('So far decoded message: ', temp_words)
                    for word in temp_words:
                        if word in valid_words:
                            if (temp_m_key) in valid_m_keys.keys():
                                valid_m_keys[temp_m_key] += 1
                            else:
                                valid_m_keys[temp_m_key] = 1
                            if (temp_c_key) in valid_c_keys.keys():
                                valid_c_keys[temp_c_key] += 1
                            else:
                                valid_c_keys[temp_c_key] = 1
            most_used_m_key = max(valid_m_keys.items(), key=operator.itemgetter(1))[0]
            most_used_c_key = max(valid_c_keys.items(), key=operator.itemgetter(1))[0]
            decoded_message = cipher.decode(message, most_used_m_key, most_used_c_key)
            print('Hacker decoded message: ', decoded_message, '\n Using keys: ', most_used_m_key, most_used_c_key)
            return decoded_message



        else:
            possible_keys = cipher.possible_keys()
            word_file = open('english_words.txt', 'r')
            valid_words = [line.rstrip('\n') for line in word_file]
            word_file.close()
            valid_keys = {}
            for temp_key in possible_keys:
                temp_message = cipher.decode(message, temp_key)
                temp_words = temp_message.split()
                for word in temp_words:
                    if word in valid_words:
                        if str(temp_key) in valid_keys.keys():
                            valid_keys[temp_key] += 1
                        else:
                            valid_keys[temp_key] = 1
            most_used_key = max(valid_keys.items(), key=operator.itemgetter(1))[0]
            decoded_message = cipher.decode(message, (most_used_key))
            print('Hacker decoded message: ', decoded_message, '\n Using key: ', most_used_key)
            return decoded_message


