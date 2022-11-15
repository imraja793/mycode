previous = 1
next = 1
my_list = [previous, next]
for i in range(10):
    my_list.append(previous+next)
    previous, next = next, previous+next
print(my_list)


#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    print(u,v,w,x)
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
my_func = partial(func, 2, 3, 4)
print(my_func(3))
