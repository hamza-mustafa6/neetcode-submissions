class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by starting time
        #compare 1st value of the element with the 2nd value of the previous element
        merged = []
        intervals.sort()
        if len(intervals) == 1:
                return intervals
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[i][1])]
    
            else: 
                merged.append(intervals[i])
        return merged