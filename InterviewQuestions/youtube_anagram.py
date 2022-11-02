def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    dict1 = {}
    
    for element in range(0,len(str1)):
        char = str1[element]
        if char not in dict1:
            dict1[char] = 0     
        dict1[char]+=1 
        
        
    for element in range(0,len(str2)):
        char = str2[element]
        if char not in dict1:
            return False
        dict1[char]-=1  
        if dict1[char]<0: 
            return False
        
    return True 

print(is_anagram('nameless','salesman')) # False
print(is_anagram('listen','silent')) # True 
print(is_anagram('xxxx','xxxxxx')) # False
print(is_anagram('triangle','integer')) # False 
print(is_anagram('geeksforgeeks','forgeeksgeeks')) # True 