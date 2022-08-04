'''
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
'''

def pair_with_targetsum(lst, target):
    p_beg = 0 
    p_end = len(lst)-1 
    
    while p_beg < p_end: 
        if target == lst[p_beg]+lst[p_end]:
            return (p_beg,p_end)
        if target < lst[p_beg]+lst[p_end]:
            p_end -= 1 
        if target > lst[p_beg]+lst[p_end]:
            p_beg += 1 
    
    return (-1,-1)


print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))