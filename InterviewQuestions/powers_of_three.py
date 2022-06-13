def power_of_three_1(test_number):
    all_three_powers_list = [3**x for x in range(30)]
    if test_number in all_three_powers_list:
        return True 
    else:
        return False  
    
def power_of_three_2(test_number):
    all_three_powers_dict = {}
    for element in range(0,20,1):
        temp_3 = 3 ** element 
        all_three_powers_dict[temp_3] = element  
    
    if test_number in all_three_powers_dict:
        return True 
    else:
        return False 
    
    
## TESTING SHOULD BE ALL TRUE 
print(power_of_three_1(1),power_of_three_1(3),power_of_three_1(59049))
## TESTING SHOULD BE ALL FALSE
print(power_of_three_1(0),power_of_three_1(2),power_of_three_1(69))
## TESTING HASHMAP function
## ALL TRUE 
print(power_of_three_2(1),power_of_three_2(3),power_of_three_2(59049))
## ALL FALSE 
print(power_of_three_2(0),power_of_three_2(2),power_of_three_2(69))