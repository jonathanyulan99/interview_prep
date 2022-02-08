
list1 = [5, 3, 15, 10, 6, 30, 7]
fizzbuzz_hashmap = {0: 'fizz or divisible by 3',
                    1: 'buzz or divisible by 5',
                    2: 'fizzbuzz or divisible by both'}


def fizzbuzz(a_list):
    for number in a_list:
        if (number % 5==0) & (number % 3==0):
            print(fizzbuzz_hashmap[2])
        elif (number % 5==0):
            print(fizzbuzz_hashmap[1])
        elif (number % 3==0):
            print(fizzbuzz_hashmap[0])
        else:
            print('Not Divisible by 3 or 5')


fizzbuzz(list1)
