from collections import deque
import random

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,value):
        self.container.append(value)
    
    ## overloaded function 
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isempty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


container_stack = Stack()

for element in range(5):
    random_num = random.randrange(0,1000)
    container_stack.push(random_num)

for element in range(0,container_stack.size(),+1):
    print(container_stack.pop())