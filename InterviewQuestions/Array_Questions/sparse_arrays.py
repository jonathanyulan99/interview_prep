'''

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings

'''

def matchingStrings(strings,queries):
    '''
    hash_map = dict()
    
    for elements in strings:
        if not hash_map.get(elements,0):
            hash_map.update({elements:1})
        else:
            num_of_times = hash_map.get(elements)
            hash_map.update({elements:num_of_times+1})

    for key,value in hash_map.items():
        print(f"key:{key} and value:{value}")
    
    for index,value in enumerate(queries):
        if value in hash_map:
            queries[index] = hash_map[value]
        else:
            queries[index] = 0 
    
    return queries 
    '''
    # alternate solution 
    lst_counter = list()
    
    for query in queries:
        lst_counter.append(strings.count(query))
    
    return lst_counter

a = ["abcde","sdaklfj","asdjf","na","basdn","sdaklfj","asdjf","na","asdjf","na","basdn","sdaklfj","asdjf"]
b = ["abcde","sdaklfj","asdjf","na","basdn"]

print(matchingStrings(a,b))
