var = list(range(1, 10))
var2 = 'abcdefghij'
expected_list = [1, 'i', 3, 'g', 5, 'e']


def rearranging_letters():
    var = list(range(1, 10))
    var2 = 'abcdefghij'
    my_list = []
    m = 0
    n = -2
    while len(var)-1 > m:
        my_list.append(var[m])
        my_list.append(var2[n])
        m += 2
        n -= 2
    print(my_list)

rearranging_letters()






