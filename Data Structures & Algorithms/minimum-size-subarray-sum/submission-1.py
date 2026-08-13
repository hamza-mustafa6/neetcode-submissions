class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        sum = 0
        l = 0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum >= target:
                minimum = min(minimum, r-l+1)
                sum -= nums[l]
                l+=1
        if minimum == float('inf'):
            return 0
        else: return minimum