class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create hashmap with key:value pair as element:count
        #Create a list where the index is frequency with size nums
        countNums = dict()
        for num in nums:
            if num in countNums:
                countNums[num]+=1
            else:
                countNums[num] = 1
        frequency = [[] for _ in range(len(nums) + 1)]
        # print(f"Count map: {countNums}")
        for num in countNums:
            count = countNums[num]
            frequency[count].append(num)
            # print(f"Current num: {num}, current count: {count}, current frequency table: {frequency}")
        result = []
        numResults = k
        for i in reversed(frequency):
            if numResults == 0:
                break
            if not i:
                continue
            if len(i) == 1:
                result.append(i[0])
                numResults-=1
            if len(i) > 1:
                for elem in i:
                    result.append(elem)
                    numResults-=1
                    if numResults == 0:
                        break
        return result


