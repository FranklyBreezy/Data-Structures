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
    def merge_linked_lists(self,a,b):
        dummy = node(0)
        tail = dummy

    # Traverse both lists and append the smaller value to tail
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

    # Append any remaining nodes
        if a:
            tail.next = a
        if b:
            tail.next = b

    # Set the head of the current list to the start of merged list
        self.head = dummy.next

list1 = linked_list()
list1.insert(1)
list1.insert(3)
list1.insert(5)

list2 = linked_list()
list2.insert(2)
list2.insert(4)
list2.insert(6)

merged_list = linked_list()
merged_list.merge_linked_lists(list1.head, list2.head)
merged_list.print()
