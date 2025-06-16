from operator import truediv


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue_right(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        return True

    def enqueue_left(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        return True

    def dequeue_left(self):
        if self.head is None:
            return None

        data = self.head.data
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        return data

    def dequeue_right(self):
        if self.tail is None:
            return None

        data = self.tail.data
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
        return data

    def peek(self):
        if self.head is None:
            return None

        return self.head.data

    def get_linked_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    # def get_linked_list_backward(self):
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #
    #     while current:
    #         print(current)
    #         current = current.prev


    def insert(self, node: Node, position: int):

        if position == 0:
            node.next = self.head
            self.head = node

        current = self.head
        prev = None
        count = 0

        while current and count < position:
            prev = current
            current = current.next
            count += 1

        prev.next = node
        node.next = current

    def pop(self):
        if self.head is None:
            return False
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        last = self.head.prev
        data = last.data
        last_prev = last.prev
        last_prev.next = self.head
        self.head.prev = last_prev

        return data

    def popfirst(self):
        if self.head is None:
            return False

        current = self.head
        while current.prev:
            current = current.prev

        data = current.data

        if current.next:
            current.next.prev = None
        else:
            self.head = None
            return data

        self.head = current.next
        return data

    def remove(self, value):
        if self.head is None:
            return None
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        prev = None

        while current:
            if current.data == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

linkedlist = Stack()
# linkedlist.enqueue_right(node1)
# linkedlist.enqueue_right(node2)
# linkedlist.enqueue_right(node3)
# linkedlist.enqueue_right(node4)
# linkedlist.dequeue()
linkedlist.enqueue_left(node1)
linkedlist.enqueue_left(node2)
linkedlist.enqueue_left(node3)
linkedlist.enqueue_left(node4)
linkedlist.dequeue_right()
linkedlist.get_linked_list()

# print(f"peek: {linkedlist.peek()}")
# # linkedlist.pop()
# # linkedlist.remove(3)
# # linkedlist.get_linked_list()
# print(linkedlist.search(3))
