"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def to_list(head):
    node = head
    new_list = []
    while node:
        new_list.append(node.value)
        node = node.next
    print(new_list)
    return head


def odd_before_even(head):
    even_linked_list = None
    odd_linked_list = None
    node = head
    while node:
        if node.value % 2 == 0:
            if even_linked_list is None:
                even_linked_list = Node(node.value)
            else:
                odd_node = even_linked_list
                while odd_node.next:
                    odd_node = odd_node.next
                odd_node.next = Node(node.value)
        else:
            if odd_linked_list is None:
                odd_linked_list = Node(node.value)
            else:
                odd_node = odd_linked_list
                while odd_node.next:
                    odd_node = odd_node.next
                odd_node.next = Node(node.value)
        node = node.next
    odd_node = odd_linked_list
    while odd_node.next:
        odd_node = odd_node.next
    odd_node.next = even_linked_list
    return odd_linked_list


def create_ll(value):
    head = Node(value[0])
    node = head
    for data in value[1:]:
        node.next = Node(data)
        node = node.next

    return head


head = create_ll([1, 2, 6, 8, 3, 4, 5, 6])
to_list(head)
to_list(odd_before_even(head))

# print(obj.to_list())






