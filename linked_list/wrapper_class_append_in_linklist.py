class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
head.next = Node(2)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        node_list = []
        node = self.head
        while node:
            node_list.append(node.value)
            node = node.next
        print(node_list)
        return node_list


# linklist = LinkedList()
# linklist.append(1)
# linklist.append(2)
# linklist.append(4)
#
# node = linklist.head
# while node:
#     print(node.value)
#
#     node = node.next
# linklist.to_list()

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")