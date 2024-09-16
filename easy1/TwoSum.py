from typing import List

class TwoSum:
    def __init__(self) -> None:
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                    return result
        return list()
    
    def backTracking(self, idx: int, nums: List[int], tmp:List[int], target: int)->bool:

        if len(tmp)==3:
            if self.sumarize(nums,tmp)==target: 
                return True
        else:
            for i in range(idx, len(nums)):
                tmp.append(i)
                if self.backTracking(i+1, nums, tmp, target): 
                    return True
                tmp.pop()
        return False        

    def sumarize(self, nums: List[int], arr: List[int]) -> int:
        sum = 0
        for i in range (0, len(arr)):
            sum = sum + nums[arr[i]];
        return sum


    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        tmp = list()
        self.backTracking(0, nums, tmp, target)    
        return tmp
