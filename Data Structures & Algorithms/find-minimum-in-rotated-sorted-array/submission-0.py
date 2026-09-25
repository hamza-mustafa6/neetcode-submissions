class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while True:
            if nums[left] <= nums[right]:
                return nums[left]
            if right - left == 1:
                if nums[left] < nums[right]:
                    return nums[left]
                else: 
                    return nums[right]
            mid = (right-left)//2 + left
            if nums[mid] < nums[right]:
                right = mid
            else: 
                left = mid+1 
                