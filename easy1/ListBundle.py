import operator
from typing import List
from collections import OrderedDict


class ListBundle:

    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[r]=nums[i]
                r+=1
        return r
    
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j
    
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

    def generatePascalTriangle(self, numRows: int):
        res = []
        def helper(level: int):
            tmp = []
            lastrow = res[-1]
            if level == numRows: 
                return
            for i in range(0, level+1):
                num1 = num2 = 0
                num1 = 0 if i==0 else lastrow[i-1]
                num2 = 0 if i==level else lastrow[i]
                tmp.append(num1 + num2)
            res.append(tmp)
            helper(level+1)  
        res.append([1])          
        helper(1)
        return res
    
    def getRowPascalTriangle(self, rowIndex: int) -> List[int]:
        res = []
        comb = 1
        for i in range(0, rowIndex+1):
            res.append(int(comb))
            comb = comb * (rowIndex - i) / (i + 1)
        return res

    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        res = majority = 0
        for i in nums:
            d[i] = 1 + d.get(i,0)
            if d[i] > majority:
                res = i
                majority = d[i]
        return res

    def maxProfit1(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    profit = prices[j]-prices[i]
                    maxprofit = max(maxprofit,profit)
        return maxprofit

    def maxProfit2(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):
            minprice = min (minprice, prices[i])
            maxprofit = max(maxprofit, prices[i]-minprice)
        return maxprofit

    def singleNumber1(self, nums: List[int]) -> int:
        dcounter = {}

        for num in nums:
            exist = dcounter.get(num, None)
            if exist is None:
                dcounter[num]=1
            else:
                dcounter[num]+=1
        
        for x,y in dcounter.items():
            if y == 1: return x

        return 0
    
    def singleNumber2(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor        

    def containsDuplicate1(self, nums: List[int]) -> bool:
        duplicated = {}
        for num in nums:
            exist = duplicated.get(num, None)
            if exist is None:
                duplicated[num]=1
            else:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        sorted = nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]: return True
        return False
    
    def containsDuplicate3(self, nums: List[int]) -> bool:
        myset = set(nums)
        if len(myset) == len(nums): return False
        return True

    def containsDuplicate4(self, nums: List[int]) -> bool:
        myset = set()
        for num in nums:
            if num in myset:
                return True
            else:
                myset.add(num)
        return False


    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    if abs(i-j)<=k:
                        return True
        return False
    
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        last = len(nums)-1

        for i in range(len(nums)):
            a = i - k if k < i else 0
            b = i + k if i + k <= last else last
            while a<i:
                if nums[i]==nums[a]:
                    return True
                a+=1
            while b>i:
                if nums[i]==nums[b]:
                    return True
                b-=1

        return False             
    
    def containsNearbyDuplicate3(self, nums: List[int], k: int) -> bool:
        diplicates = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in diplicates:
                closeness = abs(diplicates[num] - i)
                if closeness <= k: 
                    return True
            diplicates[num] = i
        return False 

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        diplicates = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in diplicates:
                closeness = abs(diplicates[num] - i)
                if closeness <= indexDiff and abs(diplicates[num]-num) <=valueDiff: 
                    return True
            diplicates[num] = i
        return False 
            
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
        return []
    

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {num: idx for idx, num in enumerate(nums) }
        for i, val in enumerate(nums):
            diff = target - val 
            second = d.get(diff, None)
            if second:
                if second != i:
                    return [i,second]
        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [i,d[diff]]
            d[val]=i
        return []
    
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range (0, len(nums)):
            for j in range (i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    new1 = [nums[i],nums[j],nums[k]]
                    if sum(new1)== 0:
                        new1.sort()
                        if new1 not in ans:
                            ans.append(new1)
        return ans
    
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        sizeNums = len(nums)
        for i, fix in enumerate(nums):
            if i>0 and nums[i-1]==fix:
                continue
            j = i + 1
            k = sizeNums-1
            while j < k:
                suma = fix + nums[j] + nums[k]
                if suma > 0: 
                    k -= 1
                elif suma < 0:
                    j += 1
                else:
                    ans.append([fix, nums[j], nums[k]])
                    j += 1
                    while nums[j-1]== nums[j] and j<k: 
                        j+=1
        return ans
    
    def duplicateZeros1(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i<len(arr)-1:
            if arr[i]==0:
                j = len(arr)-1
                while j>i:
                    arr[j]=arr[j-1]
                    j-=1
                i+=1
            i+=1       

    def duplicateZeros2(self, arr: List[int]) -> None:
        i = 0
        while i<len(arr)-1:
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                i+=1
            i+=1

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {n for n in nums1 if n in nums2}
        return list(ans)
    
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        for i in nums1:
            if i in nums2:
                ans.add(i)
        return list(ans)
    
    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))

    def intersectII_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        d = {}
        for i in nums1:
            j = d.get(i,-1) + 1
            while j < len(nums2):
                if i == nums2[j]:
                    ans.append(i)
                    d[i]=j
                    break
                j+=1
        return ans

    def intersectII_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        i = 0
        j = 0
        while i < len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                j+=1
                i+=1
            elif nums2[j] > nums1[i]:
                i+=1
            else:
                j+=1
        return ans