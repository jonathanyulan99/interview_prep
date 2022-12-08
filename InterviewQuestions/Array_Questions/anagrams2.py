from collections import Counter

def isAnagramCounter(s:str, t:str)-> bool:
    if(len(s)!=len(t)): return False 
    counter1 = Counter(s)
    counter2 = Counter(t)
    
    for each in counter1:
        if(counter1[each]!=counter2[each]): return False
    
    return True

if __name__=="__main__":
    print(isAnagramCounter('cacc','accc'))
    print(isAnagramCounter('jonathan','nahtanoj'))
    print(isAnagramCounter(' ','hello'))