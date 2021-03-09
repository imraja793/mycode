# Hamming Distance
def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    if len(str1) != len(str2):
        return None

    hamming_dist = 0

    for i_char in range(len(str1)):
        if str1[i_char] != str2[i_char]:
            hamming_dist += 1

    print(hamming_dist)
    return hamming_dist
hamming_distance('0101010100011101','0101010100010001')
hamming_distance('A gentleman','Elegant men')
hamming_distance('ACTTGACCGGG','GATCCGGTACA')
hamming_distance('shove','stove')
# hamming_distance('Slot machines', 'Cash lost in me')
hamming_distance("hamming", "eemming")