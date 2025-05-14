class Node:
    # Node creation
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    head=None
    tail=None

    def add_node(self, data):
        self.node=Node(data)
        if not LinkedList.head:
            LinkedList.head=LinkedList.tail=self.node
        LinkedList.tail.next=self.node
        LinkedList.tail=self.node



    def print_ll(self):
        self.start=LinkedList.head
        while self.start:
            print(self.start.data)
            self.start=self.start.next
        

    # def next(self):
    #     pass

ll = LinkedList()
ll.add_node(5)
ll.add_node(10)
ll.add_node(15)
ll.print_ll()




    