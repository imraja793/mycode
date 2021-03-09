"""Problem Statement
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as
arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge:

One way to solve this problem is to convert the input array into a number and then add one to it. For example,
if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits
of the output number 124.

But can you solve it in some other way?"""


def normal_method(list):
    summation = ""
    for i in list:
        summation += f'{i}'
    desired = int(summation) + 1
    new_list = []
    for data in str(desired):
        new_list.append(int(data)   )
    print(new_list)


def new_method(list):
    data = list[-1]
    if data == 9:
        return when_9(list)
    else:
        list[-1] = list[-1] + 1
    print(list)


def when_9(list, pos=-1):
    list[pos] = 0
    if -(len(list)) == pos-1 and list[0] == 9:
        list[0] = 1
        list.append(0)
        print(list)
        return list
    elif list[pos-1] == 9:
        return when_9(list, pos-1)
    else:
        list[pos-1] = list[pos-1] + 1
    print(list)
    return list


new_method([9, 9, 9, 8, 9])
normal_method([9, 9, 9, 8, 9])
new_method([1, 0, 9, 9])
normal_method([1, 0, 9, 9])
new_method([9, 9, 9])
normal_method([9, 9, 9])
