"""Welcome module
Copyright Lololol

"""

import base64


def main():
    string_input = input("Entrez votre chaine : ")

    test_array = list(string_input)
    test_ascii = []
    print(test_array)
    print('')

    for char in test_array:
        test_ascii.append(ord(char))
    print(test_ascii)


if __name__ == '__main__':
    main()
