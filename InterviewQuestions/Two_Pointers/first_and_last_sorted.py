'''Given a sorted array of integers arr and an integer target,find the index of the first and last position of target in arr. If target can't be found in arr,return [-1,-1]'''

def first_and_last(arr:list,target: int):
    # default return if not found 
    result = [-1,-1]
    target_start_position = 0 
    
    for index,value in enumerate(arr):
        if value==target: 
            target_start_position = index 
            
            while index+1 < len(arr) and arr[index+1] == target:
                index+=1
            return [target_start_position,index]

    return result 

print(first_and_last([2,4,5,5,5,5,5,7,9,9],5))
print(first_and_last([2,4,5,5,5,5,5,7,9,9],3))            
    