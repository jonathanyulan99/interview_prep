class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge_bool(Intervals):
    if len(Intervals) < 2: 
        raise Exception("Not Enough Intervals to Compare")

    Intervals.sort(key=lambda x: x.start)
    
    a_end = Intervals[0].end
    
    for i in range(1,len(Intervals)):
        b = Intervals[i]
        if b.start <= a_end:
            return True 
        else:
            a_end = max(a_end,b.end)
            
    return False

def main():
    print("The Intervals Overlap: ", end='')
    print(merge_bool([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))
    '\n'
    
    print("The Intervals Overlap: ", end='')
    print(merge_bool([Interval(6, 7), Interval(2, 4), Interval(5, 9)]))
    '\n'
    
    print("The Intervals Overlap: ", end='')
    print(merge_bool([Interval(1, 4), Interval(5, 7), Interval(8, 9)]))
    '\n'

    print("The Intervals Overlap: ", end='')
    print(merge_bool([Interval(1, 4), Interval(4, 7)]))
    '\n'

main()