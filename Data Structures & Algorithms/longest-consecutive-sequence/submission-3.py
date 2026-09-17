class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums) == 0:
            return 0
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
