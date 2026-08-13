class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #5, 4, 5
        minimum = float('inf')
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum>=target:
                    if minimum > j-i+1:
                        minimum = j-i+1
                    break; 
        if minimum == float('inf'):
            return 0
        else: return minimum