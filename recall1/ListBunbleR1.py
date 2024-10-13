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

        #starting
        for i in range(0, len(height)):
            maxleft = getmaxLeft(i)
            maxright = getmaxRight(i)
            print(f"V1 heigh:{height[i]} maxLeft:{maxleft} maxRight:{maxright}")
            if maxleft and maxright:
                area = min(maxleft, maxright) - height[i]
                if area>0: h.append(area)
        print("heights:", h)
        return sum(h)            
    
    def trapV2(self, height: List[int]) -> int:
        h = []
        maxleft = 0
        maxright = 0
        a = 0
        b = len(height)-1
        while a <= b:
            print(f"V2 heigh.a:{height[a]} height.b:{height[b]} maxLeft:{maxleft} maxRight:{maxright}", end="")

            if height[a] < height[b]:
                if height[a] > maxleft: 
                    maxleft = height[a]
                elif maxleft > height[a]:
                    areaA = maxleft - height[a]
                    if areaA>0: 
                        h.append(areaA)
                        print(f" * {areaA}",end="")
                a+=1
            else:
                if height[b] > maxright: 
                    maxright = height[b]
                elif maxright > height[b]:
                    areaB = maxright - height[b]
                    if areaB>0: 
                        h.append(areaB)
                        print(f" * {areaB}",end="")
                b-=1
            print()
        print("V2. heights:", h)
        return sum(h)
    

    def maxAreaV1(self, height: List[int]) -> int:
        res = []

        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res.append(area)
                print(f"{i}={height[i]} {j}={height[j]} area:{area}")

        print("res:", res)
        return max(res)
    
    def maxAreaV2(self, height: List[int]) -> int:
        res = []
        a = 0
        b = len(height)-1
        while a<b:
            area = (b - a) * min(height[a], height[b])
            print(f"{a}={height[a]} {b}={height[b]} area:{area}")
            res.append(area)
            if height[a] < height[b]:
                a+=1
            else:
                b-=1
        print("areas:", res)
        return max(res)
    
    def maximumTastinessV1(self, price: List[int], k: int) -> int:

        return 0