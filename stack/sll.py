class IsEmptyError(Exception):
    pass

class SLLStack: 
    class Node: 
        def __init__(self,element, _next):
            self.element = element
            self._next = _next
    
    def __init__(self):
        self.head = None
        self.size = 0 
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError('This stack is empty, can not pop')
        result = self.head.element
        self.head = self.head._next
        self.size -= 1
        return result
    
    def top(self):
        if self.is_empty():
           raise IsEmptyError('Stack is empty cannot retrieve elements') 
        return self.head.element


test = SLLStack()

# print(help(test))

test.push(1)
print(test.top())