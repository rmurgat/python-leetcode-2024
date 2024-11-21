from easy1.LinkedList1Bundle import *
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
from easy1.StringBundle import *
from easy1.BinaryBundle import * 
from easy1.NumbersBundle import *
from easy1.MyStack import *

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
    print ("Answer #1 ", lib.rob([1,2,3,1]))


def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Find Good Days to Rob a Bank (LC#2100)")
        print("2. House Robber (LC#198)")

        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printFindGoodDays()
            case 2: printHouseRobber()
            case 99: exit()

main()