Single Linked List

obj = SLinkedList()
obj.traverse_list()
obj.insert_at_start(x)
obj.insert_at_end(x)
obj.insert_after_item(item, x)
obj.insert_at_index(index, x)
param6 = obj.get_count()
bool = obj.contains(x)

class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.val , " ")
                n = n.next

    def insert_at_start(self, x):
        new_node = Node(x)
        new_node.next, self.head = self.head, new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node

    def insert_after_item(self, val, x):
        n = self.head
        while n is not None:
            if n.val == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(x)
            new_node.next = n.next
            n.next = new_node

    def insert_at_index(self, index, x):
        if index == 1:
            new_node = Node(x)
            new_node.next, self.head = self.head, new_node
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.next
            i += 1
        if n is None:
            print("Index out of bounds")
        else:
            new_node = Node(x)
            new_node.next = n.next
            n.next = new_node

     def get_count(self):
        if self.head is None:
            return 0;
        n = self.head
        count = 0;
        while n is not None:
            count += 1
            n = n.next
        return count

    def contains(self, x):
        if self.head is None:
            return False
        n = self.head
        while n is not None:
            if n.val == x:
                return True
            n = n.next
        return False

    def delete_at_start(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
