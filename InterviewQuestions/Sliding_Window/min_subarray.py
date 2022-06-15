'''Given an array of positive integers and a number "S," find the length of the smallest contiguous subarray whose sum is greater than or equal to "S". Return 0 if no such subarray exists.'''
import math

def min_subarray(S,ARR):
    # return 0 if no such subarray exists 
    temp_sum = 0 
    min_result = math.inf 
    window_begin = 0 
    
    for window_end in range(len(ARR)):
        temp_sum += ARR[window_end]
        
        #temp_sum remembers the length of this window as the smallest window so far 
        while temp_sum >= S: 
            min_result = min(min_result, window_end-window_begin+1)
            temp_sum-=ARR[window_begin]
            window_begin+=1
    
    if min_result == math.inf:
        return 0 
    return min_result 

def main():
    print("Smallest subarray length: " + str(min_subarray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(min_subarray(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(min_subarray(8, [2, 1, 5, 2, 3, 2])))
    
main()


'''Given an array of positive integers and a number "S," find the length of the smallest contiguous subarray whose sum is greater than or equal to "S". Return 0 if no such subarray exists.'''

def slide_min(TARGET,ARR):
    window_begin = 0 
    temp_min = math.inf
    sum_sub_array = 0 
    
    for window_end in range(len(ARR)):
        sum_sub_array+=ARR[window_end]
        
        while sum_sub_array >= TARGET:
            temp_min = min(temp_min, window_end-window_begin + 1)
            sum_sub_array-= ARR[window_begin]
            window_begin+=1 
    
    if temp_min == math.inf:
        return 0 
    return temp_min 
            
def main2():
    print("Smallest subarray length: " + str(slide_min(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(slide_min(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(slide_min(8, [2, 1, 5, 2, 3, 2])))
    
main2()            
            
            