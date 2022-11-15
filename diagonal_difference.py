arr = [[11,2,4], [4,5,6], [10, 8, -12]]

prim_count = 0
d1, d2 = 0, 0
for i in range(len(arr)):
    d1 += arr[i][i]
    d2 += arr[i][len(arr)-i-1]
    print(d1, d2)
sec_count = 0
for data in range(len(arr)):
    for ele in range(len(arr)):
        if data + ele == len(arr) - 1:
            sec_count += arr[data][ele]
print(abs(d1 - d2))

