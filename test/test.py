"""
Given an array of random numbers. return the array of continous sequence having max length.

input: [3, 2, 1, 6, 7, 4, 10]
output: [1,2, 3, 4]


"""
a = [3, 2, 1, 6, 7, 4, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 23, 22]
result = 0
for i in a:
    j = i
    if i-1 not in a:
        while j in a:
            j += 1
        result = max(result, j - i)
print(result)


"""
  Space : 
  Time: O(n)
"""