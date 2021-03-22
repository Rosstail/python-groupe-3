"""Welcome module
Copyright Lololol

"""


def input_checker():
    """
    Ask an input to user and return it
    :return: string_input
    """
    string_input = input("Entrez votre chaine : ")
    return string_input


def string_to_array(string):
    """
        Convert string parameter to array and returns it
    :param string:
    :return: list of string parameter
    """
    return list(string)


def string_to_ascii(string):
    """
        Convert string parameter to int array and returns it
    :param string:
    :return: array of int
    """
    array = []
    for char in string:
        print(char)
        array.append(ord(char))
    return array


def num_to_bin(number_list):
    """
        convert array of int paramater to array of string (as binary) and returns it
    :param number_list:
    :return:
    """
    array = []
    for number in number_list:
        array.append(bin(number)[2:].zfill(8))
    return array


def string_split_interval(string):
    """
        Convert string parameter to array of string then returns it.
        Each string int array is 6 chars long.
    :param string:
    :return:
    """
    split_strings = []
    n = 6
    for index in range(0, len(string), n):
        split_strings.append(string[index: index + n])


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
