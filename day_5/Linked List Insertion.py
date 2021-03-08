class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, node, data):

        if node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

   

    def printList(self):
        temp_node = self.head
        while (temp_node):
            print(str(temp_node.item) + " ", end="")
            temp_node = temp_node.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('Linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()
