from typing import List


class ListBundle:

    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[r]=nums[i]
                r+=1
        return r
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None: return 0
        for i in range(0,len(nums)):
            if target <= nums[i]:
                return i
        return len(nums) 
    
    def plusOne(self, digits: List[int]) -> List[int]:
        remanent = True
        length = len(digits)
        for i in range(length-1, -1, -1):    
            if remanent:
                digits[i] = digits[i] + 1
                if digits[i] > 9 :
                    remanent = True
                    digits[i] = 0
                else:
                    remanent = False
        if remanent:
           return [1] + digits
        return digits
