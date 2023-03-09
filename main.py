from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
    result = []
    listlen = len(nums)
    
    for i in range(0, listlen):
        for j in range(i+1, listlen):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result
    
    return result;