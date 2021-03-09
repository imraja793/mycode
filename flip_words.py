sentence = "I am a software engineer"
split_sentence = sentence.split(" ")
print(split_sentence[::-1])

reversed_list = []
position_list = len(split_sentence) - 1
while position_list >= 0:
    reversed_list.append(split_sentence[position_list])
    position_list -= 1

print(reversed_list)


def rev_sting(string):
    position = len(string) - 1
    reversed_str = ''

    while position >= 0:
        reversed_str += string[position]
        position -= 1
    return reversed_str


def flip_words(sentence):

    split_sentence = sentence.split(sep=" ")
    reversing_list = []
    length_split = 0
    while len(split_sentence) - 1 >= length_split:
        reversing_list.append(rev_sting(split_sentence[length_split]))
        length_split += 1
    print(" ".join(reversing_list))

flip_words("is it done")
