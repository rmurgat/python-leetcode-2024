from easy1.TwoNumbers import *
from easy1.TwoSum import TwoSum
from easy1.Duplicate import Duplicate
from easy1.Palindrome import Palindrome
from easy1.Romans import Romans
from easy1.LongestSubstring import LongestSubstrig
from easy1.Zigzag import Zigzag
from easy1.Conversion import Conversion
from easy1.StringBundle import StringBundle
from easy1.LinkedList1Bundle import LinkedList1Bundle
from easy1.ListBundle import ListBundle
from easy1.Combinations import Combinations
from easy1.MatrixBundle import MatrixBundle
from typing import List

def printingAddTwoNumbers():
    sol = TwoNumbers
    n1 = sol.num2ListNode("342")
    n2 = sol.num2ListNode("465")
    print('[n1:]')
    sol.printListNode(n1)
    print('[n2:]')
    sol.printListNode(n2)
    sum = sol.addTwoNumbers(n1, n2)
    print('[res:]')
    sol.printListNode(sum)

def printingTwoSum():
    sol = TwoSum()
    nums = list({1,2,3,4,5,6,7,8,9,10})
    print(sol.twoSum(nums, 9))

def printingTwoSum2():
    sol = TwoSum()
    nums = list({1,2,3,4,5,6,7,8,9,10})
    res = sol.twoSum2(nums, 9)
    print('positions: ', res)
    print('values: ', );
    for i in range(0,len(res)):
        print(nums[res[i]],end=",")

def removingDuplicates():
    sol = Duplicate()
    nums = list({1,1,2,2,3,3,4,4,2,1,3,3,3,7,8,9,9,10})
    res = sol.removeDuplicates(nums)
    print('Removing duplicates: ', res)
    print('nums:',nums[0:res])


def removingDuplicatesSet():
    sol = Duplicate()
    nums = list({1,1,2,2,3,3,4,4,2,1,3,3,3,7,8,9,9,10})
    res = sol.removeDuplicatesSet(nums)
    print('Removing duplicates: ', res)
    print('nums:',nums)

def removingStringDuplicates():
    sol = Duplicate()
    names = ["Alex","Alex","Fredy","Fredy","Lazaro","Ruben","Ruben","Javier","Javier"]
    res = sol.removeStringDuplicates(names)
    print("names:",names[0:res]);

def removingStringDuplicatesSet():
    names = ["Alex","Alex","Fredy","Fredy","Lazaro","Ruben","Ruben","Javier","Javier"]    
    tmp = set(names)
    names.clear()
    for s in tmp:
        names.append(s)
    names.sort()
    print(names)

def isStringPalindrome():
    sol = Palindrome()
    print("Is palindrome: ", sol.isPalindrome("baa"))

def reviewIfNumIsPalindrome():
    sol = Palindrome()
    print("Is palindrome: ", sol.isPalindromeInt(121))

def longestPalindromeInSubstring():
    sol = Palindrome()
    print("Longest palindrome:",sol.longestPalindrome("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))

def convertingRoman2Int():
    sol = Romans()
    print("Algo No.1: ", sol.romanToInt_1("MCMXCIV"))
    print("Algo No.2: ", sol.romanToInt_2("MCMXCIV"))
    print("Algo No.3: ", sol.romanToInt_3("MCMXCIV"))

def findingLongestSubstring():
    sol = LongestSubstrig()
    print("Find max longest Substring:")
    print("[pwwkew:]",sol.lengthOfLongestSubstring_1("pwwkew"))

def getZigzagString():
    sol = Zigzag()
    print("A,1: ", sol.convert("A", 1))

def printReverseInteger():
    sol = Conversion()
    print("reversing [1534236469:]", sol.reverseInt(1534236469))

def printatoi():
    sol = StringBundle()
    print("atoi [ ]:",  sol.myAtoi(" "))

def printLongestCommonPrefix():
    sol = LongestSubstrig()
    list = ["reflower","flow","flight"]
    print("longest[]: ", list, "->", sol.longestCommonPrefix(list))

def printValidParentheses():
    sol = StringBundle()
    print("Valid Parentheses: ", sol.isValidParentheses("(]"))

def printMergeTwoSortedLists():
    sol = LinkedList1Bundle()
    lst1 = sol.createListNode([2,6,7,8,9,10])
    lst2 = sol.createListNode([1,3,4,5,6])
    print("ListNode: [", sol.convertListNode2String(lst1),"]")
    print("ListNode: [", sol.convertListNode2String(lst2),"]")
    lstm = sol.mergeTwoLists(lst1, lst2)
    print("ListNode Merged: [", sol.convertListNode2String(lstm),"]")

def printIsPalindromeAlpha():
    sol = Palindrome()
    print("isPalindromeAlpha[0P]: ", sol.isPalindromeAlpha("0P"))
    print("isPalindromeAlpha[a]: ", sol.isPalindromeAlpha("a"))
    print("isPalindromeAlpha[ ]: ", sol.isPalindromeAlpha(" "))
    print("isPalindromeAlpha[A man, a plan, a canal: Panama]: ", sol.isPalindromeAlpha("A man, a plan, a canal: Panama"))
    print("isPalindromeAlpha[race a car]: ", sol.isPalindromeAlpha("race a car"))

def removingElementFromList():
    sol = ListBundle()
    list = [3,2,2,3]
    res=sol.removeElement(list,3)
    print("Removing 3 from list [3,2,2,3]: ", res, "=", list[0:res])

def find1stOccurrenceString():
    sol = StringBundle()
    print("Find the Index of the First Occurrence in a String:")
    print(sol.strStr("a","a"))

def searchingInsertPosition():
    sol = ListBundle()
    print("Search insert position in List")
    print("position:", sol.searchInsert([1,3,5,6],10))

def getlengthOfLastWord():
    sol = StringBundle()
    print("Length of Last Word")
    print("Length:", sol.lengthOfLastWord("a"))

def printPlusOnde():
    sol = ListBundle()
    print("Printing Plus Onde")
    print("value:", sol.plusOne([9]))

def printAddBinary():
    sol = StringBundle()
    print("Printing Add Binary")    
    print("value:", sol.addBinary("0", "0") )

def printClimbStairs():
    sol = Combinations()
    print("[ Printing Climbing Stairs ]")
    print("Conbinations[35]:", sol.climbStairs(35))

def printBetTimetoBuySellStock():
    sol = ListBundle()
    print("Printing Best Time to Buy and Sell Stock")
    print("Answer 1: ", sol.maxProfit1([7,1,5,3,6,4]), "(brute force)")
    print("Answer 2: ", sol.maxProfit2([7,1,5,3,6,4]), "(optimized)")

def printSingleNumber():
    sol = ListBundle()
    print("In Array, Every element appears twice except for one. Find that single one") 
    print("Answer 1: ", sol.singleNumber1([4,1,2,1,2]), "(brute force)")
    print("Answer 2: ", sol.singleNumber2([4,1,2,1,2]), "(XOR solution)")

def printcontainDuplicate():
    sol = ListBundle()
    print("if any value appears at least twice in the array, return True")
    print("Answer 1, Algo #1: ", sol.containsDuplicate1([4,1,2,1,2]), "(hashmap)")
    print("Answer 2, Algo #1: ", sol.containsDuplicate1([1,2,3,4,5,6,7]), "(hashmap)")
    print("Answer 1, Algo #2: ", sol.containsDuplicate2([4,1,2,1,2]), "(sorting)")
    print("Answer 2, Algo #2: ", sol.containsDuplicate2([1,2,3,4,5,6,7]), "(sorting)")
    print("Answer 1, Algo #3: ", sol.containsDuplicate2([4,1,2,1,2]), "(using ds set())")
    print("Answer 2, Algo #3: ", sol.containsDuplicate2([1,2,3,4,5,6,7]), "(using ds set()")
    print("Answer 1, Algo #4: ", sol.containsDuplicate2([4,1,2,1,2]), "(using ds set())")
    print("Answer 2, Algo #4: ", sol.containsDuplicate2([1,2,3,4,5,6,7]), "(using ds set()")

def printcontainDuplicateII():
    sol = ListBundle()
    print("Array Contain Duplicate II")
    print("Answer 1 [1,2,3,1], Algo #1: ", sol.containsNearbyDuplicate1([1,2,3,1], 3), "(brute force) & TLE")    
    print("Answer 2 [1,0,1,1] Algo #1: ", sol.containsNearbyDuplicate1([1,0,1,1],1), "(brute force) & TLE")    
    print("Answer 3 [1,2,3,1,2,3] Algo #1: ", sol.containsNearbyDuplicate1([1,2,3,1,2,3], 2), "(brute force & TLE)")    

    print("Answer 4 [99, 99], Algo #1: ", sol.containsNearbyDuplicate2([99,99], 2), "(nearby & TLE)")    
    print("Answer 5 [1,2,3,1], Algo #1: ", sol.containsNearbyDuplicate2([1,2,3,1], 3), "(nearby  & TLE)")    

    print("Answer 4 [99, 99], Algo #1: ", sol.containsNearbyDuplicate3([99,99], 2), "(hashmap & Submited Ok)")    
    print("Answer 5 [1,2,3,1], Algo #1: ", sol.containsNearbyDuplicate3([1,2,3,1], 3), "(hashmap & Submited Ok)")

def printcontainDuplicateIII():
    sol = ListBundle()
    print("Array Contain Duplicate III")

def printEverySpotContainValue():
    sol = MatrixBundle()
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    print ("Answer:",sol.checkValid(matrix))

    matrix = [[15,7,18,11,19,10,14,16,8,2,3,6,5,1,17,12,9,4,13],[17,15,9,8,11,13,7,6,5,1,3,16,12,19,10,2,4,14,18],[19,14,12,10,8,9,17,16,4,3,13,18,1,5,7,11,2,15,6],[4,2,10,15,19,16,8,9,5,3,1,11,13,14,6,18,12,17,7],[13,19,9,16,5,8,6,12,14,11,18,10,7,2,3,4,15,17,1],[4,7,18,11,17,16,5,12,10,1,15,13,14,6,19,2,3,9,8],[14,5,15,1,18,6,12,7,8,9,3,13,2,10,19,4,11,16,17],[10,3,1,8,14,19,11,18,15,13,9,12,16,17,7,4,5,2,6],[14,13,19,18,7,2,4,8,10,17,12,5,15,1,6,9,11,3,16],[19,8,10,18,16,12,11,17,4,9,7,2,5,13,15,3,6,1,14],[1,10,6,14,7,18,3,9,4,16,5,11,13,17,15,8,19,2,12],[13,10,5,16,1,19,17,3,9,11,7,8,12,6,4,2,14,15,18],[17,2,1,6,9,19,18,14,4,11,12,13,16,5,8,7,3,10,15],[1,4,10,5,13,6,18,11,3,2,15,14,16,12,17,19,8,9,7],[2,14,3,12,16,17,11,9,1,6,5,19,10,13,4,18,7,15,8],[15,9,8,18,14,13,4,12,5,17,6,1,11,16,19,3,7,2,10],[15,8,12,16,13,2,6,19,18,14,10,5,11,9,7,1,3,17,4],[15,6,17,7,5,3,1,9,19,12,10,11,16,14,18,8,2,13,4],[6,11,10,14,2,13,16,1,9,15,8,19,17,3,5,18,7,4,12]]
    print ("Answer 2:",sol.checkValid(matrix))

def print3Sum():
    sol = ListBundle()
    print ("3Sum (multi-for): ", sol.threeSum1([-1,0,1,2,-1,-4]))
    print ("3Sum (left-right pointer): ", sol.threeSum2([-1,0,1,2,-1,-4]))


def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Add Two Numbers (listnode)               13. get Zigzag string                 25. print Add Binary")
        print("2. Two Sum (forze brute)                    14. print Integer reversed            26. Climbing Stairs")
        print("3. Two Sum (backtracking)                   15. String to Integer (atoi)          27. Best Time to Buy and Sell Stock")
        print("4. Remove int Duplicates (inplace)          16. Longest Common Prefix             28. Single Number")
        print("5. Remove int Duplicates (using set)        17. Valid Parentheses                 29. Array Contains Duplicate")
        print("6. Remove string Duplicates (inplace)       18. Merge Tow Sorted Lists            30. Array Contains Duplicate II")
        print("7. Remove string Duplicates (using set)     19. Review if str is Palindrome Alpha 31. Array Contains Duplicate III")
        print("8. Review if str is Palindrome              20. Removing Element from List        2133. Check If Every Spot Contains Value (matrix)") 
        print("9. Review if num is Palindrome              21. Find first occurrence in String   15. 3Sum") 
        print("10. Longest Palindrome in Substring         22. Search Insert position")
        print("11. Converting Roman num to Int             23. Length of Last Word")
        print("12. Find max longest Substring              24. Plus One")
        print("")
        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            #case 1: printingAddTwoNumbers()
            #case 2: printingTwoSum()
            #case 3: printingTwoSum2()
            #case 4: removingDuplicates()
            #case 5: removingDuplicatesSet()
            #case 6: removingStringDuplicates()
            #case 7: removingStringDuplicatesSet()
            #case 8: isStringPalindrome()
            #case 9: reviewIfNumIsPalindrome()
            #case 10: longestPalindromeInSubstring()
            #case 11: convertingRoman2Int()
            #case 12: findingLongestSubstring()
            #case 13: getZigzagString()
            #case 14: printReverseInteger()
            #case 15: printatoi()
            #case 16: printLongestCommonPrefix()
            #case 17: printValidParentheses()
            #case 18: printMergeTwoSortedLists()
            #case 19: printIsPalindromeAlpha()
            #case 20: removingElementFromList()
            #case 21: find1stOccurrenceString()
            #case 22: searchingInsertPosition()
            #case 23: getlengthOfLastWord()
            #case 24: printPlusOnde()
            #case 25: printAddBinary()
            #case 26: printClimbStairs()
            #case 27: printBetTimetoBuySellStock()
            #case 28: printSingleNumber()
            #case 29: printcontainDuplicate()
            #case 30: printcontainDuplicateII()
            #case 31: printcontainDuplicateIII()
            case 15: print3Sum()
            case 2133: printEverySpotContainValue()
            case 99: return
            case _: print("Invalid Option")

main()
