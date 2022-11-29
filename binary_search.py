arr = [1,4,6,7,8,10]
x = 8


def binarySearch(arr:list, begin:int, end:int, x:int):

    # Check base case
    if end >= begin:

        mid = begin + (end - begin) // 2
        print()
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binarySearch(arr, begin, mid - 1, x)
        elif arr[mid] < x:
            return binarySearch(arr, mid + 1, end, x)

    else:
        # Element is not present in the array
        return False


print(binarySearch(arr, 0, len(arr), 2))