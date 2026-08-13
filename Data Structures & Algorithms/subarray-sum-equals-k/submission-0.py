class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = {}
        prefixCount[0] = 1
        sum = 0
        result = 0
        for i in range(len(nums)):
            sum+= nums[i]
            if sum - k in prefixCount:
                result += prefixCount[sum-k]
            prefixCount[sum] = prefixCount.get(sum, 0) + 1
        return result