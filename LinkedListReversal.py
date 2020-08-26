class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def reverse(self, head):

        current = head
        previous = None
        nextnode = None

        while current:

            nextnode = current.next_node
            current.next_node = previous

            previous = current
            current = nextnode

        return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = None
