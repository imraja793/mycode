s = 'aaabbbccaabb'
"""
    output = '3a3b2c2a2ab'
"""
out_str = ''
out_count = 0
new_var = s[0]
for i in range(len(s)):
    if new_var == s[i]:
        out_count += 1
        if len(s) - 1 == i:
            out_str += str(out_count) + new_var
    else:
        out_str += str(out_count) + new_var
        new_var = s[i]
        out_count = 1
print(out_str)

