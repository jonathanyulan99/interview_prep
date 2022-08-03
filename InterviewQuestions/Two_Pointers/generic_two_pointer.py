'''Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target'''

def two_points(lst,target):
    p_beg = 0 
    p_end = len(lst)-1
    result = set()
    
    while p_beg < p_end: 
        if lst[p_beg] + lst[p_end] == target:
            result.update([p_beg,p_end])
            break
        elif lst[p_beg] + lst[p_end] > target:
            p_end -= 1
        else: 
            p_beg+=1 
    
    return result 



print(two_points([1,2,3,4,5,6],6))