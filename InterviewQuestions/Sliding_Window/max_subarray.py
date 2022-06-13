'''Given an array of positive numbers and a positive number "K," find the maximum sum of any contiguous subarray of size "K".

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_sub_array_sliding_window(k,array):
    temp_max = maximum_result = 0.0
    window_start = 0
    
    for window_end in range(len(array)):
        temp_max += array[window_end]
        
        if (window_end >= k-1):
            if(temp_max >= maximum_result):
                maximum_result = temp_max
            temp_max -= array[window_start]
            window_start+=1 
    
    return maximum_result 

print(max_sub_array_sliding_window(2,[2,3,4,1,5]))