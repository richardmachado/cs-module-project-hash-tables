


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    def find(self, value):
        #! return the node with the given value
        cur = self.head
        while cur != None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None

    def delete_(self, value):
        #! if empty list
        if self.head == None:
            return None

        #! if deleting head 
        if value == self.head.value:
            old_head=self.head
            self.head = self.head.next
            return old_head  #!delete successfull
        prev = self.head
        cur = prev.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = None
                return cur

            cur = cur.next




ll = LinkedList()

ll.insert_at_head(Node(5))
        

a.next = b
b.next = c
c.next = d

cur = a

while cur != None:
    print(cur.value)
    cur = cur.next