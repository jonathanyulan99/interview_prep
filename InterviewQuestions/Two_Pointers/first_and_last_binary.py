'''Given a sorted array of integers arr and an integer target,find the index of the first and last position of target in arr. If target can't be found in arr,return [-1,-1]'''

def find_start(arr:list,target:int):
    #start_index = target, thus start is zero first value in list [0]
    if arr[0] == target:
        return 0
    start_pointer, end_pointer = 0,len(arr)
    
    while start_pointer <= end_pointer: 
        mid_pointer = (end_pointer+start_pointer)//2 
        if arr[mid_pointer] == target and arr[mid_pointer-1] < target: 
            return mid_pointer
        elif arr[mid_pointer] < target:
            start_pointer = mid_pointer + 1 
        else: 
            end_pointer = mid_pointer - 1
    #not found in our list 
    return -1 

def find_end(arr:list,target:int):
    #last_position in list = target
    if arr[-1] == target:
        return len(arr)-1
    start_pointer, end_pointer = 0,len(arr)
    
    while start_pointer <= end_pointer: 
        mid_pointer = (end_pointer+start_pointer)//2 
        if arr[mid_pointer] == target and arr[mid_pointer+1] > target: 
            return mid_pointer
        elif arr[mid_pointer] < target:
            start_pointer = mid_pointer + 1 
        else: 
            end_pointer = mid_pointer - 1
    return -1 

def first_and_last_binary(arr:list,target: int):
    if len(arr)==0 or arr[0]>target or arr[-1]<target:
        return [-1,-1]
    start = find_start(arr,target)
    end = find_end(arr,target)
    return [start,end]
    
print(first_and_last_binary([2,4,5,5,5,5,5,7,9,9],5))
print(first_and_last_binary([2,4,5,5,5,5,5,7,9,9],3))     