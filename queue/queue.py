from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()

    def __len__(self):
        return self.size




    def enqueue(self, value):
        # adds item to the back (tail) of the queue
        self.size += 1
        # calling function add to tail to add item to the back of the queue
        self.storage.add_to_tail(value)

    def dequeue(self):
        # remove and return and item in front of the queue
        # if there are items
        if self.size > 0:
            # we are reducing the size by one
            self.size -= 1
            # removing from head and returning that item
            return self.storage.remove_head()

    def len(self):
        # returns the number of items in the queue
        return self.size