class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        max = 1
        for n in nums_set:
            if n-1 in nums_set:
                continue
            else: 
                curr = n
                length = 1
                while n+1 in nums_set:
                    n+=1 
                    length+=1
                if length > max:
                    max = length
        return max
