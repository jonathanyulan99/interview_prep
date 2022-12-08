'''Given an array of integers arr and an integer k, find the kth largest element

1 <= k <= |arr| 

'''

def kth_largest_sorting(arr:list,k:int): 
    arr = sorted(arr) 
    # arr = sorted(arr) 
    # arr.sort() 
    # 9-4 = 6 
    # [1,2,3,4,5,6,7,7,9], 4th largest number in the array 
    # n = len(arr) -> n-k = index_of_kth_largest 
    return arr[len(arr)-k]
    
print(kth_largest_sorting([4,2,9,7,5,6,7,1,3],4))