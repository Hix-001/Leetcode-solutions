# 24/08/2026
# Hard
# LeetCode 352: Data Stream as Disjoint Intervals using lazy evaluation.

class SummaryRanges:
    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.nums:
            return []
            
        sorted_nums = sorted(list(self.nums))
        res = []
        start = sorted_nums[0]
        end = sorted_nums[0]
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == end + 1:
                end = sorted_nums[i]
            else:
                res.append([start, end])
                start = sorted_nums[i]
                end = sorted_nums[i]
                
        res.append([start, end])
        return res