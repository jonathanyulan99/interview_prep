def check_ana(word,array):
    # print(word,array)
    for characters in array:
        # print(characters)
        if (sorted(word)==sorted(characters)):
            return True

def funWithAnagrams(text):
    text.reverse()
    ## text = [4,poke,pkoe,okpe,ekop]
    result_string = list(text)
    ## result_string = [ekop,okpe,pkoe,poke,4]
    counter = 0
    
    for index in range(0,len(text)):
        ## check to ensure we stay in the loop
        if text[index+1:] and check_ana(text[index],text[index+1:]):
            result_string.pop(index-counter)
            counter+=1 
    
    return sorted(result_string)
    
    

str = ['code', 'doce', 'ecod', 'framer', 'frame']
print(funWithAnagrams(str))