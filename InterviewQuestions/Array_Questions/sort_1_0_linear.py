"""Given an Array of 1s and Os, Please sort them in Linear O(N) time"""

test_list = [0,1,1,1,0,0,1,0,15,1,0,1,0,0,0]

def sort_list(inp_list):
    count_0 = 0
    count_1 = 0 
    solution_list = list()
    
    for num in inp_list:
        if(num == 1): 
            count_1+=1
        elif(num == 0):
            count_0+=1
        else: 
            print("Not a 1 or 0")
            continue

    while(count_0>0):
        solution_list.append(0)
        count_0-=1

    while(count_1>0):
        solution_list.append(1)
        count_1-=1
    
    return solution_list

print(sort_list(test_list))
             