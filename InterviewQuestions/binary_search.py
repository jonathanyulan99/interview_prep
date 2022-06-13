def binary_search(sorted_list,target):
    ##this is an int thus it's always going to be rounded up due to X.5 or X.0 
    ##ex: 10/2 = 5 or 9/2 = 4.5 goes to 5 
    middle_index = int(len(sorted_list)/2)
    if(len(sorted_list)==0): return False 
    if(sorted_list[middle_index]==target):
        return True 
    ## target greater than list[middle_index] and sorted than not in lower half
    elif(target>sorted_list[middle_index]):
        ## slicing [start:end:step]
        return binary_search(sorted_list[middle_index:-1],target)
    else:
        return binary_search(sorted_list[0:middle_index],target)

target = 15
user_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(f"Does the {target} exist in our {user_list}? {binary_search(user_list,target)}") 

[1,2,3,4,5,6]