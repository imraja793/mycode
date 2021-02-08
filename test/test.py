"""
Given an array of random numbers. return the array of continous sequence having
max length.

input: [3, 2, 1, 6, 7, 4, 10]
output: [1,2, 3, 4]


"""
a = [3, 2, 1, 6, 7, 4, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 23, 22]
a.sort()
print(a)
new = set()
c = []
d = a[0]
new_list = set()
max_length = 0
for i in range(len(a)):
    if i == len(a) - 1:
        if len(new) > max_length:
            new_list = new
            max_length = len(new)
            new = set()

    if i == 0 or d == int(a[i]) - 1:
        new.add(d)
        new.add(a[i])
        d = a[i]

    else:
        if len(new) > max_length:
            new_list = new
            max_length = len(new)
            new = set()
            d = a[i]
        else:
            d = a[i]
            new = set()

print(new_list)

"""
  Space : 
  Time: O(n)
"""