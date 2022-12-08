def binary_search(target,arr):
    start = 0
    end = len(arr)
    
    while(start<=end):
        med = (end+start)//2;
        
        if(target==arr[med]):
            return med;
            ##median index
        elif(target>arr[med]):
            start = med+1;
        else:
            end=med-1;
    
    return "Does Not Exist"


list_1 = [1,2,3,4,5,6,7,8,9,10]
print(len(list_1))
print(binary_search(1,list_1))
print(binary_search(4,list_1))
print(binary_search(10,list_1))
print(binary_search(5,list_1))