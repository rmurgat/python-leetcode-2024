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
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mi = m - 1
        ni = n - 1
        right = (m+n)-1

        while ni>=0:
            if mi>=0 and nums2[ni] < nums1[mi]:
                nums1[right] = nums1[mi]
                mi = mi - 1
            else:
                nums1[right] = nums2[ni]
                ni = ni -1
            right = right -1


        

                
        

