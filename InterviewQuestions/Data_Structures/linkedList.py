class LinkedNode:
    def __init__(self,data=None,nxt=None):
        self.data = data 
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None  
        
    def insert_at_beginning(self,data):
        self.head = LinkedNode(data,self.head)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = LinkedNode(data,None)
            return
        
        itr = self.head 
        while itr.nxt:
            itr = itr.nxt 
        
        itr.nxt = LinkedNode(data,None)
    
    def insert_values(self,lst):
        for element in lst:
            self.insert_at_end(element)
            
    def get_len(self):
        if self.head is None:
            raise Exception("No LinkedList")

        counter = 0 
        itr = self.head 
        while itr:
            counter+=1
            itr = itr.nxt
        
        return counter
    
    def insert_at_index(self,index,data):
        if (index < 0) or (index > self.get_len()):
            raise Exception("Out Of Bounds")
        
        if self.head is None or index==0:
            self.insert_at_beginning(data)
        
        counter = 0 
        itr = self.head
        while itr:
            if counter == index - 1:
                node = LinkedNode(data,itr.nxt)
                itr.nxt = node 
                break
            
            itr = itr.nxt 
            counter+=1

    def print(self):
        if self.head is None:
            raise Exception("Linked List is Empty")
            return 
        
        exp_string = ''
        itr = self.head 
        while itr:
            exp_string+=str(itr.data) + "-->"
            itr = itr.nxt
        
        print(exp_string) 

if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert_at_beginning(12)
    linkedList.insert_at_index(0,1)
    linkedList.insert_at_index(2,15)
    linkedList.print()
            
        