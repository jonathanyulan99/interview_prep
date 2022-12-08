'''Given an array of integers arr and an integer k, find the kth largest element

1 <= k <= |arr| 

'''

my_list = [1,10,34,234,123,14,4,6,7,8,0,167,15,143]

my_new_list = [-element for element in my_list]


print(f'before:{my_list}')
print(f'after:{my_new_list}')
print(f'SORTED AFTER:{sorted(my_new_list)}')
print(f'SORTED BEFORE:{sorted(my_list)}')


# heap priority que in Python based on smallest value, not largest value...thus reverse the order using negative values 
from heapq import * 
import heapq 

def heapq_kth_largest(arr:list,k:int): 
    arr = [-element for element in arr]
    heapq.heapify(arr)
    # item = heappop(heap) # pops the smallest item from the heap
    for item in range(k):
        item = heapq.heappop(arr)
    
    return -item
    
print(heapq_kth_largest([4,2,9,7,5,6,7,1,3],4))
print(f'First Largest in the Big List: {heapq_kth_largest(my_list,1)}')
print(f'Third Largest in the Big List: {heapq_kth_largest(my_list,3)}')
print(f'Third Largest in the Big List: {heapq_kth_largest(my_list,2)}')