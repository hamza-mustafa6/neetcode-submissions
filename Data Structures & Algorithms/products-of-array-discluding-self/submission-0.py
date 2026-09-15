class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        prefix_arr = [1] * arr_len
        suffix_arr = [1] * arr_len

        prefix_sum = 1
        for i in range (1, arr_len):
            prefix_sum = prefix_sum * nums[i-1]
            prefix_arr[i] = prefix_sum
        
        suffix_sum = 1
        for i in range (arr_len-2, -1, -1):
            suffix_sum = suffix_sum * nums[i+1]
            suffix_arr[i] = suffix_sum

        for i in range(arr_len):
            prefix_arr[i] = prefix_arr[i] * suffix_arr[i]

        return prefix_arr
               