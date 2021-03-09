class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

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
        node = self.head
        new_list = []
        while node:
            new_list.append(node.value)
            print(new_list)
            node = node.next

        return new_list

    def check_circular(self):
        fast = self.head
        slow = self.head
        while fast.next:
            if fast.next == slow:
                print("loop is present")
                return
            slow = slow.next
            fast = fast.next.next

            
list_with_loop = LinkedList([1, 2, 34, -1, 5])
loop_start = list_with_loop.head.next
node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start
# list_with_loop.to_list()
list_with_loop.check_circular()
