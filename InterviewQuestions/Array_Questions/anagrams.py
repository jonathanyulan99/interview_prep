def isAnagram(s:str,t:str) -> bool:
    if(len(s)!=len(t)):
        return False
    list1 = []
    list2 = list()
    
    list1[:0] = s 
    list2[:0] = t 
    list1.sort()
    list2.sort()
    
    if(list1!=list2):
        return False 
    
    return True 

## Alternatively you can use a Counter(string s, string t) to create a dictionary with the counter of each value in the list 

print(isAnagram('god','odg'))
print(isAnagram('abcdef','ffffff'))
print(isAnagram('nahtanoj','jonathan'))

if __name__=='__main__':
    print(isAnagram(' ','tar'))
    print(isAnagram('anagram','nagaram'))
    print(isAnagram('cacc','accc'))