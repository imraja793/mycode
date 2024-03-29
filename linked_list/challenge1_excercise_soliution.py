
def list_to_string(input_list: list) -> str:
    string = str()
    string = "".join((str(i) for i in input_list))
    return string


def string_add_one(string: str) -> str:
    number = int(string)
    number += 1
    return str(number)


def string_to_list(string: str) -> list:
    return [int(char) for char in string]


def add_one(input_list: list) -> list:
    return string_to_list(string_add_one(list_to_string(input_list)))

#%% Test zone

a = [9,9,9]
test = add_one(a)

print(test)