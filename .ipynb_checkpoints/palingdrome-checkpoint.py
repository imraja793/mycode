from nose.tools import assert_equal


def palindrome(phrase):
    new_string = ""
    for data in range(len(phrase)-1, -1, -1):
        new_string += phrase[data]
    if new_string == phrase:
        return new_string
    return new_string


assert palindrome("madam") == 'madam'


