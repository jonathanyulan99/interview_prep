'''
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

'''

def insert(Intervals,New_Interval):
    merge = []
    itr, start, end = 0,0,1 
    
    while itr < len(Intervals) and Intervals[itr][end] < New_Interval[start]:
        merge.append(Intervals[itr])
        itr+=1 
    
    while itr < len(Intervals) and Intervals[itr][start] <= New_Interval[end]:
        New_Interval[start] = min(New_Interval[start], Intervals[itr][start])
        New_Interval[end] = max(New_Interval[end], Intervals[itr][end])
        itr+=1 
    
    merge.append(New_Interval)
    
    while itr < len(Intervals):
        merge.append(Intervals[itr])
        itr+=1 
    
    return merge

def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()