a = "duiehiuegwgiheoejpl"

out_dict = {}
res_keys = {}
for data in a:
    if data in out_dict.keys():
        out_dict[data] = int(out_dict[data]) + 1
    else:
        out_dict[data] = 1
    res_keys[data] = res_keys.get(data, 0) + 1

print(out_dict)
print(res_keys)
