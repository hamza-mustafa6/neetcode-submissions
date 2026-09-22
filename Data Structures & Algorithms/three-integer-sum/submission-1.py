class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)-2):
            left_p = i + 1
            right_p = len(nums_sorted)-1

            if i > 0:
                if nums_sorted[i] == nums_sorted[i-1]:
                    continue
            while left_p < right_p:

                sum = nums_sorted[i] + nums_sorted[left_p] + nums_sorted[right_p]
                if sum > 0:
                    right_p -=1
                if sum < 0:
                    left_p +=1
                if sum == 0:
                    result.append([nums_sorted[i], nums_sorted[left_p], nums_sorted[right_p]])
                    left_p +=1
                    while left_p<right_p and nums_sorted[left_p] == nums_sorted[left_p-1]:
                        left_p +=1
               
        return result