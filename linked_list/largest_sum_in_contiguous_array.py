from functools import reduce


def sum_arr(array):
    result = reduce(lambda x, y: x+y, array)
    # result = 0
    # for integers in array:
    #     result += integers
    return int(result)


def get_array(given_list):
    list_sum = 0
    new_list = list()
    given_list_len = len(given_list)
    for i in range(given_list_len):
        for j in range(i+1, given_list_len+1):
            sum_arr_result = sum_arr(given_list[i:j])
            if sum_arr_result > list_sum:
                list_sum = sum_arr_result
                new_list = given_list[i:j]
    print(list_sum, new_list)

get_array([1,2,3,4])
arr = [1, 2, -5, -4, 1, 6]
get_array(arr)

