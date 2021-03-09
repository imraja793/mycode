class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return self.head
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return value

    def reverse(self):
        node = self.head
        previous = None
        nextnode = None

        while node:

            nextnode = node.next
            node.next = previous

            previous = node
            node = nextnode

        self.head = previous

    def to_list(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        return node


linklist = LinkedList()
linklist.append(1)
linklist.append(2)
linklist.append(3)
linklist.append(4)
linklist.append(5)
linklist.to_list()
linklist.reverse()
print('-'*100)
linklist.to_list()

