'''
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

'''

from __future__ import print_function

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')
    

def merge(Intervals):
    merged = list()
    
    if len(Intervals) < 2: 
        return Intervals 
    
    Intervals.sort(key=lambda x: x.start)
    
    a_start = Intervals[0].start
    a_end = Intervals[0].end 
    
    for x in range(1,len(Intervals)):
        b = Intervals[x]
        # Case Merge
        if b.start <= a_end:
            a_end = max(b.end,a_end)
        else: 
            merged.append(Interval(a_start,a_end))
            a_start = b.start
            a_end = b.end 
        
    merged.append(Interval(a_start,a_end))
    return merged 

def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()
    
main() 