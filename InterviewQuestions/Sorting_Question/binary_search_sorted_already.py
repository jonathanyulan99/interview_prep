'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: list(int), target: int) -> int:
        right = len(nums)-1
        left = 0 
        
        while left<=right:
            mid = (right+left)//2 ##int 
            if(target==nums[mid]):
                return mid
            if(target>nums[mid]):
                left = mid+1
            else:
                right = mid-1
        
        return -1 