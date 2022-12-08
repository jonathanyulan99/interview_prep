# Longest Substring Without Repeating Characters
'''Given a string s, find the length of the longest substring without repeating characters.'''

def lengthOfLongestSubstring(s:str)->int:
    left_ptr = 0
    hset_substring = set()
    longest = 0
    
    for right_ptr in range(len(s)):
        while left_ptr < len(s)-1 and s[right_ptr] in hset_substring:
            hset_substring.remove(s[left_ptr])
            left_ptr += 1
        hset_substring.add(s[right_ptr])
        longest = max(longest,right_ptr-left_ptr+1)
    return longest

print(lengthOfLongestSubstring("abdcedef"))