

# Objective - your python program should print the recurring words and their count in the given string.
# Condition - No Dictionary, No Collection, No Set, No lambda, No Regular Expression, No specialized libraries
string = "Hello World Hello World I am a programmer"


for i in range(len(string)):
    new_str = string.split(" ")
    asd = []
    for i in range(len(new_str)):
        count = 1
        if new_str[i] in asd:
            count += 1
            pass
        else:
            asd.append(new_str[i])
        print()





    # if i == len(string) - 1:
    #     pass
    # elif string[i] == string[i+1]:
    #     key = string[i]
    #     count = 0
    #     j = i
    #     while string[j] and key == string[j]:
    #         count += 1
    #         j += 1
    #     print(count, string[i])



