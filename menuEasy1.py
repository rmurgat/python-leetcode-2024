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

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Add Two Numbers (listnode)               13. get Zigzag string                 25. print Add Binary")
        print("2. Two Sum (forze brute)                    14. print Integer reversed            26. Climbing Stairs")
        print("3. Two Sum (backtracking)                   15. String to Integer (atoi)")
        print("4. Remove int Duplicates (inplace)          16. Longest Common Prefix")
        print("5. Remove int Duplicates (using set)        17. Valid Parentheses")
        print("6. Remove string Duplicates (inplace)       18. Merge Tow Sorted Lists")
        print("7. Remove string Duplicates (using set)     19. Review if str is Palindrome Alpha")
        print("8. Review if str is Palindrome              20. Removing Element from List") 
        print("9. Review if num is Palindrome              21. Find first occurrence in String") 
        print("10. Longest Palindrome in Substring         22. Search Insert position")
        print("11. Converting Roman num to Int             23. Length of Last Word")
        print("12. Find max longest Substring              24. Plus One")
        print("")
        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printingAddTwoNumbers()
            case 2: printingTwoSum()
            case 3: printingTwoSum2()
            case 4: removingDuplicates()
            case 5: removingDuplicatesSet()
            case 6: removingStringDuplicates()
            case 7: removingStringDuplicatesSet()
            case 8: isStringPalindrome()
            case 9: reviewIfNumIsPalindrome()
            case 10: longestPalindromeInSubstring()
            case 11: convertingRoman2Int()
            case 12: findingLongestSubstring()
            case 13: getZigzagString()
            case 14: printReverseInteger()
            case 15: printatoi()
            case 16: printLongestCommonPrefix()
            case 17: printValidParentheses()
            case 18: printMergeTwoSortedLists()
            case 19: printIsPalindromeAlpha()
            case 20: removingElementFromList()
            case 21: find1stOccurrenceString()
            case 22: searchingInsertPosition()
            case 23: getlengthOfLastWord()
            case 24: printPlusOnde()
            case 25: printAddBinary()
            case 26: printClimbStairs()
            case 99: return
            case _: print("Invalid Option")

main()
