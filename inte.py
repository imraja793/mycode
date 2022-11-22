with open("/tmp/syslog.txt", 'r') as f:
    print("dkdnk")
    a = f.readlines()
    print(a)
    print(a)
    print(f.read(5))
    count = 0
    for data in a:
        if 'err' in data:
            count += 1
    print(count)

a = [1, 2, 2, 3, 4, 5, 5, 3]
out_list = []
for i in range(len(a)):

    if i == 0 and a[i] != a[i + 1]:
        out_list.append(a[i])
    elif i == len(a)-1 and a[i] != a[i-1]:
        out_list.append(a[i])
    elif a[i] != a[i+1] and a[i] != a[i-1]:
        out_list.append(a[i])
print(out_list)

