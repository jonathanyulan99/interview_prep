'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''
def two_sum(nums:list[int],target:int)->list[int]:
    dict_container = dict()
    
    for idx,num in enumerate(nums):
        if(target-num in dict_container):
            return (dict_container.get(target-num),idx)        
        dict_container.update({num:idx})
    
    
    
    
print(two_sum([3,2,4],6))