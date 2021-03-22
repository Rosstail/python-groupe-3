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
    return split_strings


def fill_six_content(string_array):
    """
        fill each string in string_array with "0" if string length < 6.
        Returns the filled array
    :param string_array:
    :return:
    """
    array = []
    for content in string_array:
        while len(content) < 6:
            content = content + "0"
        array.append(content)
    return array


def array_string_to_number(string_array):
    """
        Convert string values of string_array parameter to int and return array
    :param string_array:
    :return:
    """
    int_array = []
    for string in string_array:
        int_array.append(int(string, 2))
    return int_array


def array_number_to_chr(int_array):
    """
        Convert int values of int_array parameter to characters and returns it
    :param int_array:
    :return:
    """
    chr_array = []
    for value in int_array:
        chr_array.append(chr(65 + value))
    return chr_array


def chr_array_to_string(chr_array):
    """
        Concat chr_array parameter to string and returns it
    :param chr_array:
    :return:
    """
    return ''.join(chr_array)


def string_length_to_multiple(string):
    """
        Add "=" chars to string parameter if not multiple of 4 and returns it
    :param string:
    :return:
    """
    while int(len(string) / 4) != 0:
        print(int(len(string) / 4))
        string = string + "="
    return string


def main():
    string_input = input_checker()

    test_array = string_to_array(string_input)  # Ex 1
    print(test_array)

    test_array = string_to_ascii(test_array)  # Ex 2
    print(test_array)

    test_array = num_to_bin(test_array)  # Ex 3 and 4
    print(test_array)

    test_array = ''.join(test_array)  # Ex 5
    print(test_array)

    six_array = string_split_interval(test_array)  # Ex 6
    print(six_array)

    six_array = fill_six_content(six_array)  # Ex 7
    print(six_array)

    six_array = array_string_to_number(six_array)  # Ex 8
    print(six_array)

    six_array = array_number_to_chr(six_array)  # Ex 9
    print(six_array)

    six_string = chr_array_to_string(six_array)  # Ex 10
    print(six_string)

    #six_string = string_length_to_multiple(six_string)  # Ex 11
    #print("test " + six_string)


if __name__ == '__main__':
    main()
