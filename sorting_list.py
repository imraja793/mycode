a = [2, 1, 12, 22, 1, 55]
so_list = []

while a:
    b = a[0]
    for element in a:
        if b < element:
            b = element
    print(so_list)
    so_list.append(b)
    a.remove(b)
print(so_list)

a = 'raja'
count = 0
out_list = set()
for data in a:
    for i in a:
        if data == i:
            count += 1
    out_list.add((data, count))
    count = 0
print(out_list)


def spam():
    global eggs
    eggs += 1
    print(eggs)


eggs = 343
spam()
print(eggs, "hff")



