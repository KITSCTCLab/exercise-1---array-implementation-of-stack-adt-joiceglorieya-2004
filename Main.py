import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items)== 0

    def is_full(self):
       return len (self .items) >=self.size

    def push(self, data):
        if not self.is_full():
            self.items.append(data)
                         
    def pop(self):
        if not self.is_empty():
            self .removed-element =self.items.pop()
            
     def status(self):
        for numbers in self.items:
            print(numbers)

  
