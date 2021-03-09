class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.list = [1,2,3,4,5,5,6]


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


def creating_linklist(list):
    head = None
    tail = None
    for value in list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            print(tail.value)
            tail.next = Node(value)
            tail = tail.next
    return head


input_list = [1, 2, 3, 4, 5, 6]
head = creating_linklist(input_list)
test_function(input_list, head)
