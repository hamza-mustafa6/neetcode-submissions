class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()

        for i in range(len(nums)):
            # if target - curr exists, return, else, add curr to dictionary and continue
            num = nums[i]
            if num_map.get(target - num, "not found") != "not found":
                if target - num == num:
                    return [num_map.get(target - num), i]
                    
                num_map[num] = i
                return [num_map.get(target - num), num_map.get(num)]
            else:
                num_map[num] = i