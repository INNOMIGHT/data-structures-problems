# Assuming you already have a Linked List
class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def cycle_check(node):
        marker_1 = node
        marker_2 = node

        while(marker_2 != None and marker_2.next_node != None):
            marker_1 = marker_1.next_node
            marker_2 = marker_2.next_node.next_node

            if(marker_2 == marker_1):
                return True

        return False
