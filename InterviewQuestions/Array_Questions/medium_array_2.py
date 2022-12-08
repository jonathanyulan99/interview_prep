'''
DIFF: Medium
TYPE: ARRAY 

You are given an array of positive integers where each integer \
represents the heights of a vertical line on a chart. Find two lines
which together with the x-axis forms a container that would hold the greatest amount of water. Return the area of water it could hold

ex - [1,8,6,2,9,4]
Solution here is the 8 and the 9 
Imagine A Bar Graph with the list numbers as height
Area = L * W
AREA = 8 * 3 
AREA = 24 maxiumum area we can form from two lines in the bar graph

STEP 1: VERIFY THE CONSTRAINTS w/ Clarifying Questions 

1. Does the thickness of the lines affect the area? 
    No

2. Do the left and right sides of the graph counts as walls? 
    No, sides cannot be used to form a container. Only the values in the list can be used. 

3. Does a higher line inside our container affect our area? 
    No, lines do not impact the area. No lines inside the chosen container, will be impacted by the other lines. 

STEP 2: WRITE OUT TEST CASES

1. [7,1,2,3,9] 
    7 and 9 greatest apart, and the biggest numbers in the list
        The second value, is the maxiumum height that can be possible
    7 is the smallest of the two numbers, so its the \
        highest the wall can be
    Figuring out the width? 
        Subtract the indices 
    Indices: 
        4 = 9 
        0 = 7 
        4-0 = length
    ANSWER:
        7 minimum of the two numbers
        Indices Difference = 4 - 0 = 4 
        7 * 4 = 28 
        28 
2. [ ] = return 0

3. [any singular value] = return 0 
  
4. [6,9,3,4,5,8] -> not an intuitive direct solution
   [0 1 2 3 4 5] -> indices     
    6 and 8 possible solution #1
        5-0 = length
        min(6,8) = 6 
        L * W = AREA
        L = index_diff(6,8) = index(8) - index(0) or 5-0 = 5
        W = min(6,8) = 6
        6 * 5 = Area
        30 = Area
    
    9 and 8 possible solution #2
        5-1 = length
        min(8,9) = 8
        8 * 4 = Area 
        32 = Area

STEP 3: Figure out a solution without a code (LOGICAL)

INDEX- [0 1 2 3 4] 
 LIST- [7,1,2,3,9]
 GREATEST OR LEAST MEANS RUN THROUGH THE ENTIRIETY OF THE / DATASET
AREA = length * width 
LENGTH = min(a,b)
    a - left pointer
    b - right pointer
Width = (b_index - a_index)
AREA = min(a,b) * (b_index - a_index)
[7,1,2,3,9]
 a b

max_area = 0 
    min(7,1) * (1-0)
    max_area = 1 * 1 
    max_area = 1
    old_max_area < new_max_area 
        replace 
    old_max_area > new_max_area
        keep it the same 

NEXT ITERATION
[7,1,2,3,9]
 a   b  
min(7,2) * (2-0) = new_max_area
    new_max_area > old_max_area
        replace
    else: 
        move to the next iteration
[7,1,2,3,9]
 a       b
 min(7,9) * (4-0) = new_max_area
    new_max_area = 28
    new_max_area > old_max_area
        replace
    else:
        continue iteration

NOW 
[7,1,2,3,9]
   a b
    ** WE HAVE MOVED THE A POINTER NOW 
    min(1,2) * (2-1) = 1 
    old_max_area = 28 
    new_max_area = 1 
    old_max_area > new_max_area:
        move b pointer 
...

[7,1,2,3,9]
   a     b
    min(1,9) * (4-1) = 3 
    28 > 3 
    reset the A pointer 

[7,1,2,3,9]
     a b
     min(2,3) * (3-2) = 2 
     28 > 2 
     move the B pointer 
AND SO ON....
[7,1,2,3,9]
     a   b
...
[7,1,2,3,9]
       a b
       28 REMAINS THE GREATEST AREA
       max_area = 28
'''

# Solution1
# container
list_1 = [7,1,2,3,9]
max1 = list_1.__len__()

# variables 
old_max_area = 0
max = len(list_1)

for element in list_1:
    new_max_area = 0
    if (list_1.index(element)+1) == max:  
        a = b = list_1[-1]
        print(a, b, max)
    else: 
        a = element
        a_pointer = list_1.index(a)
        b = list_1[a_pointer+1]
        print(a, b)
    
print(f'MAX IS {max1}')