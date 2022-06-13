def isPower(arr):
    # Write your code here
    answer = []
    # for element in arr:
    #     if (element==0):
    #         answer.append(0)
    #     while element!= 1:
    #         if(element%2 != 0):
    #             answer.append(0)
    #         element = element/2
    #     answer.append(1)
    for num in arr:
        if(num and(not(num & (num-1)))):
            answer.append(1)
        else:
            answer.append(0)
    return answer 