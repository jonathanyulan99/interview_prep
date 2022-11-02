'''Given an array, find the average of all subarrays of "K" contiguous elements in it.

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5 '''  

def slide_window_averages(k,array):
    result = list()
    window_sum = 0.0
    window_start = 0 
    
    for window_end in range(len(array)):
        window_sum+=array[window_end]
        
        # index 0 array
        # thus k = 5, length = 6 
        # if we want 5 array elements, we need index[0-4]
        if(window_end >= k - 1):
            result.append(window_sum/k)
            window_sum-=array[window_start]
            window_start+=1
    
    return result

print(slide_window_averages(5,[1,3,2,6,-1,4,1,8,2]))