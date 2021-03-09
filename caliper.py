previous = 1
next = 1
my_list = [previous, next]
for i in range(10):
    my_list.append(previous+next)
    new = next
    next = previous + next
    previous = new


print(my_list)
