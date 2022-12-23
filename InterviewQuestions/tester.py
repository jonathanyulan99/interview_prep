import sys

size = 10
heap = [0] * size
root = 0
heap[root] = (sys.maxsize)

print(heap)

dic = {'hello': 1, 'you': 2, 'are': 3, 'so': 4, 'to': 5}

for key, val in dic.items():
    print(key, val,end=' ')

print('\n')

dic = dic.fromkeys(dic,sorted(dic.values(),reverse=True))
i=0

for key in dic:
    print("Iteration:{} Key:{} and Value:{}".format(i,key,dic[key]),end=' ')
    i+=1