from solutions.TwoSum import TwoSum
from solutions.Duplicate import Duplicate
from solutions.Palindrome import Palindrome
from solutions.Romans import Romans
from typing import List

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

def reviewIfNumIsPalindrome():
    sol = Palindrome()
    print("Is palindrome: ", sol.isPalindromeInt(121))

def convertingRoman2Int():
    sol = Romans()
    print("Algo No.1: ", sol.romanToInt_1("MCMXCIV"))
    print("Algo No.2: ", sol.romanToInt_2("MCMXCIV"))
    print("Algo No.3: ", sol.romanToInt_3("MCMXCIV"))
        

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Two Sum (forze brute)")
        print("2. Two Sum (backtracking)")
        print("3. Remove int Duplicates (inplace)")
        print("4. Remove int Duplicates (using set)")
        print("5. Remove string Duplicates (inplace)")
        print("6. Remove string Duplicates (using set)")
        print("7. Review if num is Palindrome") 
        print("8. Converting Roman Number to Int (1,2,3)")
        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printingTwoSum()
            case 2: printingTwoSum2()
            case 3: removingDuplicates()
            case 4: removingDuplicatesSet()
            case 5: removingStringDuplicates()
            case 6: removingStringDuplicatesSet()
            case 7: reviewIfNumIsPalindrome()
            case 8: convertingRoman2Int()
            case 99: return
            case _: print("Invalid Option")

main()