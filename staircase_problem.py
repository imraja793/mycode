n=6
list_comp = []
req_str = ''
for i in range(n):
    for j in range(n):
        if i + j >= n-1:
            req_str += '*'
        else:
            req_str += ' '
    print(req_str)
    req_str = ''


arr= [1,2,3,4,5]
b = arr.sort()
c = arr[0:4]
d = arr[1:5]
min_sum = 0
max_sum = 0
for data in range(4):
    min_sum += c[data]
    max_sum += d[data]
print(max_sum, min_sum)



candles = [3,2,1,3]
b = candles[0]
out_dict = {}
for data in candles:
    if data > b:
        out_dict[data] = 1
        b = data
    if data == b:
        if data in out_dict:
            out_dict[data] = out_dict[data] + 1
        else:
            out_dict[data] = 1

print(b)
n = out_dict[b]
print(n)
s = '12:00:01PM'
s = s.split(':')

if 'AM' in s[2]:
    if s[0] == '12':
        s[0] = '13'
else:
    if s[0] == '12':
        s[0] = '13'
    else:
        s[0] = int(s[0]) + 12
s[2] = s[2][0:2]
req = ''
print(f'{s[0]} : {s[1]} : {s[2]}')

print(f'{s[0]} : {s[1]} : {s[2]}')