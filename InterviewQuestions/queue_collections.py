from collections import deque

##append()->
##<-appenleft()
## FIFO vs LIFO
## First In -> Comes Out First 

q = deque()

q.appendleft("first")
q.appendleft(20)
q.appendleft("last")

print(q.pop(),q.pop(),q.pop())

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self,value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    ## helper method
    ## len == 0 means empty
    def is_empty(self):
        return len(self.buffer)==0

    ## helper method 
    ## returns size 
    ## returns capacity+1 = size 
    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({'company':'Walmart','price':563.45})
pq.enqueue({'company':'Cola','price':415.45})
pq.enqueue({'company':'Naruto','price':435.45})

print(pq.buffer)
print(pq.dequeue(),pq.dequeue(),pq.dequeue())
print(pq.buffer)