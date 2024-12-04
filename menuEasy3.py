from easy1.LinkedList1Bundle import *
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
from easy1.StringBundle import *
from easy1.BinaryBundle import * 
from easy1.NumbersBundle import *
from easy1.MyStack import *
from easy1.IntervalBundle1 import *

import math

def printFindGoodDays():
    lib = ListBundle()
    print("Answer #1: ", lib.goodDaysToRobBank([5,3,3,3,5,6,2], 2))
    print("Answer #1: ", lib.goodDaysToRobBank([28,27,13,19,23,4,29,29,7], 2))
    print("Answer #2: ", lib.goodDaysToRobBank([1,1,1,1,1], 0))
    print("Answer #3: ", lib.goodDaysToRobBank([1,2,3,4,5,6], 2))
    print("Answer #3: ", lib.goodDaysToRobBank([4,3,2,1], 1))
    print("Answer #3: ", lib.goodDaysToRobBank([1,2,3,4],0))

def printHouseRobber():
    lib = ListBundle()
    print ("Answer #1: ", lib.rob([1,2,3,1]))

def printMergetIntervals():
    lib = IntervalBundle1()
    print ("Answer #1: ", lib.merge([[1,3],[2,6],[15,18],[8,10]]))
    print ("Answer #2: ", lib.merge([[1,4],[4,5]]))

def printInsertInterval():
    lib = IntervalBundle1()
    print ("Answer #1: ", lib.insert([[1,3],[6,9]],[2,5]))
    print ("Answer #2: ", lib.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))

def printNonOverlapingIntervals():
    lib = IntervalBundle1()
    print ("Answer #1: ", lib.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print ("Answer #2: ", lib.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print ("Answer #3: ", lib.eraseOverlapIntervals([[1,2],[2,3]]))
    print ("Answer #4: ", lib.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    print ("Answer #5: ", lib.eraseOverlapIntervals([ [0,1], [1,2], [3,4] ]))
    print ("Answer #6: (expected=9) ", lib.eraseOverlapIntervals([[-3035,30075],[1937,6906],[11834,20971],[44578,45600],[28565,37578],[19621,34415],[32985,36313],[-8144,1080],[-15279,21851],[-27140,-14703],[-12098,16264],[-36057,-16287],[47939,48626],[-15129,-5773],[10508,46685],[-35323,-26257]]))

    

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Find Good Days to Rob a Bank (LC#2100)      21. Merge Intervals (LC#56) ")
        print("2. House Robber (LC#198)                       22. Insert Interval (LC#57) ")
        print("3.                                             23. non-overlaping Intervals (LC#435)")
        

        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printFindGoodDays()
            case 2: printHouseRobber()

            case 21: printMergetIntervals()
            case 22: printInsertInterval()
            case 23: printNonOverlapingIntervals()
            case 99: exit()

main()