class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()

        for i in range(len(nums)):
            # if target - curr exists, return, else, add curr to dictionary and continue
            num = nums[i]
            if num_map.get(target - num, "not found") != "not found":
                return [num_map.get(target - num), i]
            else:
                num_map[num] = i