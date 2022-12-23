def twoArrays(k:int, A:list, B:list)->str:
    ''' There are two n-element arrays of integers, A and B. Permute them into some A` and B` such that the relation A`[i] + B`[i] >= k holds for all i where 0 <= i < n. '''
    
    assumed_values_b = [0] * (len(A)-1) 
    
    for ind,val in enumerate(A):
        assumed_values_b.insert(ind,abs(k-val))
    if sum(assumed_values_b) <= sum(B):
        return "Yes" 
    else:
        return "No" 
        


lst1 = [1,2,2,1]
lst2 = [3,3,3,4]

print(twoArrays(5,lst1,lst2))
print(twoArrays(10,[2,1,3],[7,8,9]))
print(twoArrays(10,[7,6,8,4,2],[5,2,6,3,1]))
help(twoArrays)