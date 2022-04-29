def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else: 
        return fib(n-1)+fib(n-2)

print(fib(10))

## Top-Down-Memoization
def calcFib(n):
    # This just returns an array of numbers that is one larger than the size of the inputted value
    # if n = 5 
    # [-1 for x in range(6)]
    # range(6) -> 0, 1, 2, 3, 4, 5 indexes return goes to the number BUT DOES NOT include that index
    # This works because we start at indexing zero(0)
    # [-1,-1,-1,-1,-1,-1]
    #  0, 1, 2, 3, 4, 5 
    memoize = [-1 for x in range(n+1)]
    return calculateFibonacciRecursion(memoize,n)

def calculateFibonacciRecursion(memoize,n):
    if n < 2:
        return n
    
    #if we already SOLVED the problem in an earlier iteration, simply return from the cache 
    if memoize[n] >=0: 
        return memoize[n]
    
    memoize[n] = calculateFibonacciRecursion(memoize,n-1) + calculateFibonacciRecursion(memoize,n-2)
    return memoize[n]


print(calcFib(10))

def fibTabulation(n):
    
    # The table, this can only contain two values, note that these are the very first instances of the the fibonacci sequence
    fib_dp_table = [0,1]
    
    # here we start at 2, because we know that if it isn't two, the answer is one of the two values listed in our fib_dp_table
    for i in range(2,n+1):
        #We append() here to attach at the end of our container
        fib_dp_table.append(fib_dp_table[i-1]+fib_dp_table[i-2])
    
    return fib_dp_table[n]

print(fibTabulation(10))
        
        
        
        