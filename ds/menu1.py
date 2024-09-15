from solutions.TwoNumbers import *
from solutions.TwoSum import TwoSum
from solutions.Duplicate import Duplicate
from solutions.Palindrome import Palindrome
from solutions.Romans import Romans
from solutions.LongestSubstring import LongestSubstrig
from solutions.Zigzag import Zigzag
from solutions.Conversion import Conversion
from solutions.StringUtils import StringUtils
from solutions.LinkedList1Bundle import LinkedList1Bundle
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
    sol = StringUtils()
    print("atoi [ ]:",  sol.myAtoi(" "))

def printLongestCommonPrefix():
    sol = LongestSubstrig()
    list = ["reflower","flow","flight"]
    print("longest[]: ", list, "->", sol.longestCommonPrefix(list))

def printValidParentheses():
    sol = StringUtils()
    print("Valid Parentheses: ", sol.isValidParentheses("(]"))

def printMergeTwoSortedLists():
    sol = LinkedList1Bundle()
    lst1 = sol.createListNode([2,6,7,8,9,10])
    lst2 = sol.createListNode([1,3,4,5,6])
    print("ListNode: [", sol.convertListNode2String(lst1),"]")
    print("ListNode: [", sol.convertListNode2String(lst2),"]")
    lstm = sol.mergeTwoLists(lst1, lst2)
    print("ListNode Merged: [", sol.convertListNode2String(lstm),"]")

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Add Two Numbers (listnode)               13. get Zigzag string")
        print("2. Two Sum (forze brute)                    14. print Integer reversed")
        print("3. Two Sum (backtracking)                   15. String to Integer (atoi)")
        print("4. Remove int Duplicates (inplace)          16. Longest Common Prefix")
        print("5. Remove int Duplicates (using set)        17. Valid Parentheses")
        print("6. Remove string Duplicates (inplace)       18. Merge Tow Sorted Lists")
        print("7. Remove string Duplicates (using set)")
        print("8. Review if str is Palindrome") 
        print("9. Review if num is Palindrome") 
        print("10. Longest Palindrome in Substring")
        print("11. Converting Roman num to Int")
        print("12. Find max longest Substring")
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
            case 99: return
            case _: print("Invalid Option")

main()