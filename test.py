"""
Given an array of random numbers. return the array of continous sequence having max length.

input: [3, 2, 1, 6, 7, 4, 10]
output: [1,2, 3, 4]


"""


def max_sequence():
    a = [3, 2, 1, 6, 7, 4, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 23, 22]
    s = set()
    ans = 0
    for data in a:
        s.add(data)

    for i in range(len(s)):

        if a[i] - 1 not in s:
            j = a[i]
            while (j in s):
                j += 1
            ans = max(ans, j-a[i])
    print(ans)


max_sequence()



