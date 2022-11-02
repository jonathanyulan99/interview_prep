def pair_with_targetsum_2(arr,target): 
    container_values = {} 
    
    for index, element in enumerate(arr):
        if target - element in container_values: 
            return (container_values[target-element],index)
        else:
            container_values[element] = index 
            
    #not found
    return (-1,-1)
    
print(pair_with_targetsum_2([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum_2([2, 5, 9, 11], 11))