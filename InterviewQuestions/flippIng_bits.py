# i: 31 , 30, 29, 28, 27, 26 ....
# if it was 9 in bits, you need (2**n) to cover 9 bits
# 2**0 = 1 : 2**1=2 : 2**2=4 : 2**3=8
# 1000 => 8
# 1st step: if i is 3, then 2**3 = 8
# 2nd step: 8/8 == 1
# 3rd step: invert because it is a '1' bit by having x is 0
# 4th step: subtract that number from 8 leaving you with 0
# 5th step: result number is the 2**i or 8 times '0' to simulate the '1' bit being flipped to '0'
def flipping_bits(n:int)->int:
    result = 0
    for i in range(31,-1,-1):
        if n>0 and n//(2**i)==1:
            x = 0 
            n-=2**i 
        else:
            x=1 
        result += (2**i) * x 
    
    return result 

def flippingBits(n):
    result = 0

    for i in range(31, -1, -1):
        # the iteration we are on is able to get into the number we are passing
        # we only need to know if it goes into the number for the logic to work
        # we subtract the number from it if it does go into the number
        # we return that number returned if it is '1' bit initally it needs to get               # flipped to '0'
        if n//(2**i) == 1:
            # we want to invert the 1, cause it does go into it
            x = 0
            # get your new n
            n -= (2**i)
        else:
            # it didn't go in which means we want this number in the result
            # we want our '0' to be a '1'
            x = 1
        result += (2**i) * x if x == 1 else 0

    return result


print(flipping_bits(0))
print(flippingBits(0))
