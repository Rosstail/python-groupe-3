"""Welcome module
Copyright Lololol

"""

import base64


def input_checker():
    string_input = input("Entrez votre chaine : ")
    return string_input


def string_to_array(string):
    return list(string)


def string_to_ascii(string):
    array = []
    for char in string:
        print(char)
        array.append(ord(char))
    return array


def num_to_bin(number_list):
    array = []
    for number in number_list:
        array.append(bin(number)[2:].zfill(8))
    return array


def main():
    string_input = input_checker()

    test_array = string_to_array(string_input)
    print(test_array)

    test_array = string_to_ascii(test_array)
    print(test_array)

    test_array = num_to_bin(test_array)
    print(test_array)

    test_array = ''.join(test_array)
    print(test_array)


if __name__ == '__main__':
    main()
