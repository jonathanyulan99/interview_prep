'''Given an array of integers arr and an integer k, find the kth largest element

1 <= k <= |arr| 

'''

# O(KN) Solution Very Slow 
def kth_largest(arr:list,k:int):
    starter = 0 
    
    while starter < k -1 : 
        arr.remove(max(arr))
        starter+=1 
    
    return max(arr) 

print(kth_largest([4,2,9,7,5,6,7,1,3],4))
