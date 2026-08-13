class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for item in nums:
            print(item)
            if(item in myDict):
                return True 
            myDict[item] = None
            

        return False