string = "I am a good boy"
b = ''
for i in range(len(string)-1, -1, -1):
    print(string[i])
    b += string[i]
print(b)

string = "who am i"
def rev_sting(string):
    position = len(string) - 1
    reversed_str = ''

    while position >= 0:
        reversed_str += string[position]
        position -= 1

    print(reversed_str, "function wise")

