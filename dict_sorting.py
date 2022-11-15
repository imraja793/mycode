a = [{"dep":"IT","rank":3}, {"dep":"HR","rank":1}, {"dep":"QA","rank":4}]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]['rank'] > a[j]['rank']:
            a[i], a[j] = a[j], a[i]
print(a)

b = {"rank3": 2, "rank2": 3, "rank4": 1, "rank1": 4}
x = {k: v for k, v in sorted(b.items(), key=lambda a: a[0])}
print(x)
x = {k: v for k, v in sorted(b.items(), key=lambda item: item[1])}
print(x)
# db.a.find($sort:{$rank})
b = {"c": 2, "b": 3, "d": 1, "a": 4}

for k, v in sorted(b.items(), key=lambda item: item[0], reverse=True):
    print(k,v)

for k in b.items():
    print(k[1])