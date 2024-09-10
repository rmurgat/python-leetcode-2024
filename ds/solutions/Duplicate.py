from audioop import rms
from typing import List

class Duplicate:

    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j

    def removeDuplicatesSet(self, nums: List[int]) -> int:
        tmp = set(nums)
        nums.clear()
        for n in tmp:
            nums.append(n)        
        nums.sort()
        return len(nums)
    
    
    def removeStringDuplicates(self, names: List[str]) -> int:
        j=1
        for i in range(1,len(names)):
            if names[i]!=names[i-1]:
                names[j] = names[i]
                j+=1
        return j