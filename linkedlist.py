class Item:
    def __init__(self, itemname, price):
        self.itemname = itemname
        self.price = price
 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
 
    def display(self):
        current = self.head
        while current:
            print(f'Item: {current.data.itemname}, Price: {current.data.price}')
            current = current.next
 
ll = LinkedList()
ll.append(Item("Item1", 10.99))
ll.append(Item("Item2", 5.49))
ll.display()