class HashTable:
    def __init__(self):
        ## .Max is based off the buckets 
        self.Max = 10
        ## list comprehension used in order to quickly instantiate 100 array a[]
        ## .array is used for instantiating the buckets for our HashTable 
        ## self.array = [None for i in range(self.Max)]
        ## having the [] list allows for the possibility of appending to the bucket if there is a collision 
        self.array = [[] for i in range(self.Max)]
        
    # def put(self,key,value):
    #     hash_value = self.get_hash(key)
    #     self.array[hash_value] = value
        
    # def get(self,key):
    #     hash_value = self.get_hash(key)
    #     return self.array[hash_value]
        
    def __setitem__(self,key,value):
        hash_value = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.array[hash_value]):
            if len(element)==2 and element[0]==key:
                self.array[hash_value][idx] = (key,value)
                found = True
                break
        if not found:
            self.array[hash_value].append((key,value))
        
    def __getitem__(self,key):
        hash_value = self.get_hash(key)
        for element in self.array[hash_value]:
            if element[0]==key:
                return element[1]
    
    def __delitem__(self,key):
        hash_value = self.get_hash(key)
        for index, element in enumerate(self.array[hash_value]):
            ## its very important to understand that these are Python tuples
            ## tuples are immutable; this is why we don't reference the index in this for loop when coupled with the enumerate() 
            ## element[0] or tuple[0] is always the key
            ## element[1] or tuple[1] is always the value 
            ## once we see the proper key in our array, we can focus on deleting that specific instance from our list of tuples
            if element[0] == key:
                del self.array[hash_value][1]
    
    ## ASCI - ORD(key) simple hash function     
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.Max
    


def new_func(HashTable):
    tester = HashTable()
    tester["march 6"] = 120
    tester["march 6"] = 78
    tester["march 7"] = 67
    tester["march 9"] = 4
    tester["march 10"] = 88
    tester["march 17"] = 459
    print(tester.array)
    del tester["march 17"]
    print(tester.array)

new_func(HashTable)
