"""
Roman numerals are represented by seven different symbols: I,V,X,L,C,DandM.
SymbolValue
I1
V5
X10
L50
C100
D500
M1000
For example, 2is written asII in Roman numeral, just two ones added together.12is written as XII, which is simplyX + II.
 The number27is written asXXVII, which isXX + V + II.
Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is notIIII. Instead, the number four is written asIV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written asIX. There are six instances where subtraction is used:
Ican be placed beforeV(5) andX(10) to make 4 and 9. iv ix
Xcan be placed beforeL(50) andC(100) to make 40 and 90.
Ccan be placed beforeD(500) andM(1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
# iv

def convert_to_integer(num:str):
    a = {"i": 1, 'v': 5, 'x': 10, "l": 50}
    int_value = 0
    for i in range(len(num)):
        if i + 1 < len(num) and a[num[i]] < a[num[i+1]]:
            int_value -= a[num[i]]
        else:
            int_value += a[num[i]]
    return int_value

print(convert_to_integer('xxiv'))

