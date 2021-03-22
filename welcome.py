"""Welcome module
Copyright Lololol

"""


def input_getter():
    """
    Ask an input to user and return it
    :return: string_input
    """
    string_input = input("Entrez votre chaine : ")
    return string_input


def string_to_array(value):
    """
        Convert string parameter to array and returns it
    :param value:
    :return: list of string parameter
    """
    return list(value)


def string_to_ascii(values):
    """
        Convert string parameter to int array and returns it
    :param values:
    :return: array of int
    """
    ascii_values = []
    for char in values:
        ascii_values.append(ord(char))
    return ascii_values


def num_to_bin(number_values):
    """
        convert array of int paramater to array of string (as binary) and returns it
    :param number_values:
    :return:
    """
    array = []
    for number in number_values:
        array.append(bin(number)[2:].zfill(8))
    return array


def string_split_interval(value, n):
    """
        Convert string parameter to array of string then returns it.
        Each string int array is 6 chars long.
    :param value:
    :return:
    """
    split_strings = []
    for index in range(0, len(value), n):
        split_strings.append(value[index: index + n])
    return split_strings


def fill_six_content(string_values):
    """
        fill each string in string_array with "0" if string length < 6.
        Returns the filled array
    :param string_values:
    :return:
    """
    array = []
    for content in string_values:
        while len(content) < 6:
            content = content + "0"
        array.append(content)
    return array


def unfill_height_content(string_values):
    """
        fill each string in string_array with "0" if string length > 8.
        Returns the filled array
    :param string_values:
    :return:
    """
    array = []
    for content in string_values:
        if len(content) > 8:
            content = content[:-8 + len(content)]
        array.append(content)
    return array


def array_bin_to_number(string_values):
    """
        Convert string values of string_array parameter to int and return array
    :param string_values:
    :return:
    """
    int_array = []
    for string in string_values:
        int_array.append(int(string, 2))
    return int_array


def array_number_to_chr(int_values):
    """
        Convert int values of int_array parameter to characters and returns it
    :param int_values:
    :return:
    """
    chr_values = []
    for value in int_values:
        chr_values.append(chr(65 + value))
    return chr_values


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
    while int(len(string) % 4) != 0:
        string = string + "="
    return string


def one_to_ten():
    string_input = input_getter()

    test_array = string_to_array(string_input)  # Ex 1
    print(test_array)

    test_array = string_to_ascii(test_array)  # Ex 2
    print(test_array)

    test_array = num_to_bin(test_array)  # Ex 3 and 4
    print(test_array)

    test_array = ''.join(test_array)  # Ex 5
    print(test_array)

    six_array = string_split_interval(test_array, 6)  # Ex 6
    print(six_array)

    six_array = fill_six_content(six_array)  # Ex 7
    print(six_array)

    six_array = array_bin_to_number(six_array)  # Ex 8
    print(six_array)

    six_array = array_number_to_chr(six_array)  # Ex 9
    print(six_array)

    six_string = chr_array_to_string(six_array)  # Ex 10
    print(six_string)

    six_string = string_length_to_multiple(six_string)  # Ex 11
    print(six_string)


def ten_to_one():
    string_input = input_getter()

    string_input = string_length_to_multiple(string_input)  # Ex 11
    print(string_input)

    test_array = string_to_array(string_input)  # Ex 10
    print(test_array)

    test_array = num_to_bin(test_array)  # Ex 9
    print(test_array)



    #FIN DE CODE
    string_to_ascii()
    chr_array_to_string("") #ETAPE 1


def main():
    value = input_getter()
    if value.__eq__("normal"):
        one_to_ten()
    elif value.__eq__("reverse"):
        ten_to_one()


if __name__ == '__main__':
    main()
