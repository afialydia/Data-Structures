from singly_linked_list import LinkedList
from sll import SLLStack
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value) 
#         self.size += 1

#     def pop(self, value ):
#         if self.size > 0: 
#             self.size -= 1
#             self.storage.pop(value)
#             return value
#         else: 
#             return value

class Stack(SLLStack):
    def __init__(self, element = None, _next = None, head = None, size = None ):
        super().__init__(element, _next,head,size)

        self.storage = []

    # def __len__(self):
    #     return self.size

    # def push(self, value):
    #     self.storage.append(value) 
    #     self.size += 1

    # def pop(self, value ):
    #     if self.size > 0: 
    #         self.size -= 1
    #         self.storage.pop(value)
    #         return value
    #     else: 
    #         return value

            

print(help(Stack))