def anagram_checker(str1, str2):
    string1 = str1.replace(" ", "").lower()
    string2 = str2.replace(" ", "").lower()
    if len(string1) == len(string2):
        for element in string1:
            if element in string2:
                string2 = string2.replace(element, "", 1)
                pass
            else:
                print(False)
                exit()
        print(True)
        exit()
    else:
        print(False, "element")


anagram_checker('Slot machines', 'Cash lost in me')
anagram_checker("raja", "raaj")

