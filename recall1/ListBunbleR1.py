from typing import List

class ListBundleR1:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2find = target - nums[i]
            for j in range(i+1,len(nums)):
                if num2find == nums[j]:
                    return [nums[i],nums[j]]
        return []
    
    def backtracking(self, nums: List[int], idx: int, positions: int, tmp: List[int], target: int) -> bool:
        if len(tmp)==positions: 
            return True if sum(tmp)==target else False
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            if self.backtracking(nums, i+1, positions, tmp, target): return True 
            tmp.pop()
        return False

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        res = []
        self.backtracking(nums,0,2,res,target)
        return res
    
    def threeSum(self, nums: List[int], target: int):
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==target:
                        res.append(nums[i])
                        res.append(nums[j])
                        res.append(nums[k])
        return res
        
    def twoSumV3(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        res = []
        while p1 < len(nums):
            num2find = target - nums[p1]
            print ("num2find:", num2find)
            try:
                idx = nums.index(num2find, p1+1)
                res = [p1, idx]
                break
            except ValueError:
                pass
            p1+=1
        return res

    def twoSumV4(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
    
    def twoSumV5(self, nums: List[int], target: int) -> List[int]:
        a = 0; b = len(nums)-1
        while a<b:
            sum = nums[a]+nums[b]
            if sum == target:
                return [a,b]
            if sum < target:
                a+=1
            else:
                b-=1
        return []
    
    def getMaxWaterContainer(self, nums: List[int]) -> int:
        maxvol = 0
        for i in range(len(nums)-1) :
            for j in range(i+1,len(nums)):
                v = (j-i) * min(nums[i], nums[j])
                maxvol = max(maxvol,v)
        return maxvol
    
    def getMaxWaterContainerV2(self, nums: List[int]) -> int:
        maxvol = 0
        a = 0
        b = len(nums)-1
        while a<b:
            heigh = min(nums[a], nums[b])
            base = b-a
            area = base * heigh
            maxvol = max(maxvol, area)
            if nums[a] <= nums[b]:
                a+=1
            else:
                b-=1
        return maxvol
    
    def playAsong(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            print(f"{nums[i]}, ",end="")

    def trapV1(self, height: List[int]) -> int:
        # calculating volumen in each valley
        h = []
        maxLeft = 0
        maxRight = 0

        def getmaxLeft(pos: int) -> int:
            if pos==0 : return 0
            res = 0
            for j in range(pos-1, -1, -1):
                res = max(res,height[j])
            return res

        def getmaxRight(pos: int) -> int:
            res = 0
            for j in range(pos+1, len(height)):
                res = max(res,height[j])
            return res

        for i in range(0, len(height)):
            maxLeft = getmaxLeft(i)
            maxRight = getmaxRight(i)
            print(f"heigh:{height[i]} maxLeft:{maxLeft} maxRight:{maxRight}")
            if maxLeft and maxRight:
                area = min(maxLeft, maxRight) - height[i]
                if area>0: h.append(area)
        print("heights:", h)
        return sum(h)            
    
    def trapV2(self, height: List[int]) -> int:
        return 0