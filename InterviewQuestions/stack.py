class Stack:
    def __init__(self):
        self.array = []
    
    def pop(self):
        head = self.array[-1]
        self.array[-1] = None
        return head
    
    def push(self,value):
        self.array.append(value)
        
    def peek(self):
        head = self.array[-1]
        return head 
    
    def p(self):
        reverse = []
        for element in self.array:
            reverse.insert(0,element)
        
        for element in reverse: 
            print(element)
            print("---------")
        

test = Stack()
test.push(5)
test.push(12)
test.push(16)
test.p()
print(test.peek())