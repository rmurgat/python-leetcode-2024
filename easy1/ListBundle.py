import operator
import math
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
    
    def threeSumClosest_1(self, nums: List[int], target: int) -> int:
        nsize = len(nums)
        answer = 0
        mindiff3 = float('inf')
        for i in range (0,nsize-2):
            for j in range (i+1, nsize-1):
                for k in range (j+1, nsize):
                    sum3 = nums[i] + nums[j] + nums[k]
                    diff3 = abs(target - sum3)
                    #print ("3 vals [", nums[i], nums[j], nums[k], "] sum3:", sum3, " diff3:", diff3)
                    if diff3 < mindiff3:
                        mindiff3 = diff3
                        answer = sum3
        return answer
    
    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        answer = {"res":0,"min":float('inf')}
        mindiff3 = float('inf')

        def ThreeSum(start: int, l3: List[int], answer):
            if len(l3) == 3:
                sum3 = sum(l3)
                diff3 = abs(target - sum3)
                #print ("l3 ", l3," sum3: ", sum3, " diff3: ", diff3)
                if diff3 < answer["min"]:
                    answer["min"] = diff3
                    answer["res"] = sum3

            for i in range (start, len(nums)):
                l3.append(nums[i])
                ThreeSum(i+1, l3, answer)
                l3.pop()

        ThreeSum(0,[], answer)

        return answer["res"]
    
    def threeSumClosest_3(self, nums: List[int], target: int) -> int:
        nums.sort()
        last = len(nums)
        mind = float('inf')
        answer = 0
        for i in range (0, last):
            low = i+1
            hight = last-1
            while low < hight:
                sum3 = nums[i]+nums[low]+nums[hight]
                dist = abs(target-sum3)
                if dist < mind:
                    mind = dist
                    answer = sum3
                if sum3 < target:
                    low+=1 
                elif sum3 > target:
                    hight-=1 
                elif sum3 == target:
                    return target
        return answer

    def letterCombinations_1(self, digits: str) -> List[str]:
        if digits == "": return []
        keys = []
        answer = []
        d = {2:"abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9:"wxyz"}
        for digit in digits:
            chars = d.get(int(digit),None)
            if chars:
                keys.append(chars)

        def combination(keys: List[str], digit: int, comb: str, answer: List[str]):
            if digit == len(keys):
                answer.append(comb)
            else:
                for char in keys[digit]:
                    combination(keys, digit + 1, comb + char, answer)
        combination(keys, 0, "", answer)
        return answer  
    
    # https://leetcode.com/problems/summary-ranges/
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums: return []
        start = 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 < nums[i]:
                ans.append(f"{nums[start]}" if start==i-1 else f"{nums[start]}->{nums[i-1]}" )
                start = i
        ans.append(f"{nums[start]}" if start==len(nums)-1 else f"{nums[start]}->{nums[len(nums)-1]}")
        return ans
  
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range (len(nums)):
            product = 1
            for j in range (0,len(nums)):
                if i != j:
                    product = product * nums[j]
            ans.append(product)
        return ans
    
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = 1
        for i in range(len(nums)):
            ans[i] = left
            left = left * nums[i]
        right = 1
        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = right * ans[i]
            right = right * nums[i]
        return ans
    
    def fourSum_1(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        long = len(nums)
        for i in range (long-3):
            if i>0 and nums[i]==nums[i-1]: 
                continue
            for j in range (i+1,long-2):
                if j>i+1 and nums[j]==nums[j-1]: 
                    continue
                left = j + 1
                right = long-1
                while left < right:
                    suma = nums[i]+ nums[j]+ nums[left]+ nums[right]
                    if suma < target:
                        left+=1
                    elif suma > target:
                        right-=1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left+=1                            
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
        return ans


    def nextPermutation_1(self, nums: List[int]) -> None:
        ans = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                for k in range (len(nums)):
                    if i!=j and j!=k and i!=k:
                        ans.append([nums[i],nums[j],nums[k]])
        idx = ans.index(nums)
        if idx < len(ans)-1:
            print( ans[idx+1] )
        else:
            print( ans[0] )


    def nextPermutation_2(self, nums: List[int]) -> None:
        print(nums)

        def swap(nums: List[int], i):
            one = i-1
            if i==0: one = len(nums)-1
            tmp = nums[one]
            nums[one] = nums[i]
            nums[i] = tmp

        for i in range(len(nums)-1,1,-1):
            swap(nums,i)
            print(nums)
            
        for i in range(0,len(nums)-1):
            swap(nums,i)
            print(nums)

    def searchInRotated(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = math.floor((right-left)/2) + left
            if nums[mid]==target:
                return  mid
            if nums[mid] >= nums[left]:  #sorted
                if nums[left]<=target<=nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:  #sorted
                if nums[mid]<=target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
    
    #34. Find First and Last Position of Element in Sorted Array
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last = -1
        low = 0
        top = len(nums)-1
        while low<=top:
            mid = math.floor((top-low)/2) + low
            if nums[mid]==target:
                i = mid
                while i>=0 and nums[i]==target:
                    first = i
                    i-=1
                i = mid
                while i<len(nums) and nums[i]==target:
                    last = i
                    i+=1
                break
            elif nums[mid]>target:
                top = mid - 1
            else:
                low = mid + 1
        return [first,last]
    
    # https://leetcode.com/problems/jump-game/
    def canJump_1(self, nums: List[int]) -> bool:
        d = {}
        def jump(nums, pos) -> bool:
            if pos == len(nums)-1: return True
            if pos > len(nums)-1: return False
            if nums[pos]==0: return False
            for i in range (1, nums[pos]+1):
                explored = d.get(pos+i, False)
                if not explored and jump(nums, pos+i): 
                    return True
                else:
                    d[pos+1] = True
            return False
        return jump(nums, 0)
    
    # https://leetcode.com/problems/jump-game/
    def canJump_2(self, nums: List[int]) -> bool:
        d = {}
        stack = [0]
        l = len(nums)-1
        while len(stack)>0:
            pos = stack.pop()
            if pos == l: return True
            if pos < l and nums[pos] != 0:
                processed = d.get(pos,False)
                if not processed:
                    for i in range (1, nums[pos]+1):
                        processed1 = d.get(pos+i,False)
                        if not processed1: stack.append(pos+i)
                    d[pos] = True
        return False

    # https://leetcode.com/problems/combination-sum/
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        anset = set()

        def backtracking(start: int, tmp: List[int]):
            if sum(tmp) > target:
                return
            if sum(tmp) == target:
                anset.add(tuple(sorted(tmp[:])))
                return

            for i in range (0, len(candidates)):
                tmp.append(candidates[i])
                backtracking(i+1, tmp) 
                tmp.pop()

        backtracking(0, [])
        return [list(x) for x in anset]

    # https://leetcode.com/problems/permutations/
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        L = len(nums)
        def backtracking():
            if L==len(tmp):
                ans.append([nums[t] for t in tmp])
                return
            for i in range(0, L):
                if i not in tmp:
                    tmp.append(i)
                    backtracking()
                    tmp.pop()
            return
        backtracking()
        return ans 

    def permuteRaw_1(self, n: int, k: int) -> List[List[int]]:
        ans = []
        tmp = []
        def backtrack():
            if len(tmp)==k:
                ans.append(tmp[:])
                return
            for i in range(1,n+1):
                if i not in tmp:
                    tmp.append(i)
                    backtrack()
                    tmp.pop()
        backtrack()
        return ans

    # https://leetcode.com/problems/combinations/description/
    def combine_1(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start: int, tmp: List[int]):

            if len(tmp)==k:
                ans.append(tmp.copy())
                return

            for i in range(start, n+1):
                tmp.append(i)
                backtrack(i+1, tmp)
                tmp.pop()

        backtrack(1, [])

        #print (ans)

        return ans

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        ans = []
        tmp = []
        def backtrack(start: int):
            if len(tmp)==k:
                ans.append(tmp[:])
                return
            for i in range(start, n+1):
                tmp.append(i)
                backtrack(i+1)
                tmp.pop()
        backtrack(1)
        return ans
    
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        L = len(security)
        goodays = []
        beforedays = [0] * L
        afterdays = [0] * L

        for i in range (1, L):
            if security[i] <= security[i-1]:
                beforedays[i] = beforedays[i-1] + 1

        for i in range (L-2, -1, -1):
            if security[i] <= security[i+1]:
                afterdays[i] = afterdays[i+1] + 1

        for i in range (time,L-time):
            if beforedays[i]>=time and afterdays[i]>=time:
                goodays.append(i)

        return goodays
    
    def combinationSum2_1(self, candidates: List[int], target: int) -> List[List[int]]:
        L = len(candidates)    
        answer = set()
        def backtracking (sublst: list):
            vals = [candidates[x] for x in sublst ]
            if sum(vals) == target:
                vals.sort()
                answer.add(tuple(vals[:]))
                return
            if sum(vals) > target:
                return
            for i in range (L):
                if i not in sublst:
                    sublst.append(i)
                    backtracking(sublst)
                    sublst.pop()
        backtracking([])
        return [list(x) for x in answer]

    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
        L = len(candidates)
        candidates.sort()
        answer = []

        def backtracking(lstmp: List[int], cur: int, left: int):
            if left == 0:
                answer.append(lstmp[:])
                return

            for i in range(cur, L):
                if i>cur and candidates[i]==candidates[i-1]: continue
                if candidates[i]>left: continue
                lstmp.append(candidates[i])
                backtracking(lstmp, i+1, left - candidates[i])
                lstmp.pop()

        backtracking([],0,target)
        return answer
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        L = len(nums)

        def backtracking(tmp: List):
            if len(tmp)==L:
                answer.add(tuple([nums[x] for x in tmp]))
                return

            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]: continue
                if i not in tmp:
                    tmp.append(i)
                    backtracking(tmp)
                    tmp.pop()

        backtracking([])
        return [list(x) for x in answer]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = "".join(sorted(s))
            located = d.get(ss,None)
            if located:
                d[ss].append(s)
            else:
                d[ss] = [s]
        return [ x for x in d.values() ]

        
    def maxSubArray_0(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        L = len(nums)
        maxi = nums[0]
        for i in range (0,L):
            last = 0
            for j in range (i, L):
                if nums[j] + last > maxi:
                    maxi = nums[j] + last
                last = nums[j] + last
        return maxi
    
    # Kadane's Algorithm - https://www.simplilearn.com/kadanes-algorithm-article
    def maxSubArray_1(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = 0
        for n in nums:
            max_ending_here = max(n, n + max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far  


    def rob(self, nums: List[int]) -> int:
        


        return 0

