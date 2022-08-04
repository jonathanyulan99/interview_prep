from collections import Counter

def sum_2D_array(arr):
    result = 0 
    for index, lst in enumerate(arr):
        for element in arr[index]:
            result+=element 

    return result 

def sum_2D_array_2(arr):
    result_list = list(map(sum,arr))
    return sum(result_list)


print(sum_2D_array([[0,1,2,3,4,5],
                    [1,2,3,4,5],
                    [1,2,3,4,5,6]]))

print(sum_2D_array_2([[0,1,2,3,4,5],
                    [1,2,3,4,5],
                    [1,2,3,4,5,6]]))