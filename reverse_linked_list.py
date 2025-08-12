class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def insert(self,val):
        new_node = node(val)
        if self.head == None:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = new_node
    def remove(self,val):
        if self.head == None:
            print("Linked List has not been initialised")
            return 0
        else:
            ptr = self.head
            if ptr.val == val:
                self.head = ptr.next
                return 0
            while ptr.next != None:
                prev_ptr = ptr    
                ptr = ptr.next
                if ptr.val == val:
                    prev_ptr.next = ptr.next
                    return 
            print(f"{val} to be removed is not stored in Linked List.")
    def print(self):
        if self.head == None:
            print("Linked List has not been initialised.")
            return 0
        else:
            ptr = self.head
            while ptr != None:
                print(ptr.val)
                ptr = ptr.next
    def reverse_linked_list(self):
        if self.head == None:
            print("Linked list is empty.")
            return 0
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
         
a = linked_list()
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)
a.print()
a.reverse_linked_list()
a.print()
