from recall1.ListBunbleR1 import ListBundleR1

def printingSumTwo():
    sol = ListBundleR1()
    print("to list [1,4,7,9,2,6]")
    print("res.v2 (11):",sol.twoSumV2([1,4,7,9,2,6],11))
    print("res.v3 (11):",sol.twoSumV3([1,4,7,9,2,6],11))
    print("res.v4 (11) hash table:",sol.twoSumV4([1,4,7,9,2,6],11))
    print("to list [1,2,4,6,7,9] sorted")
    print("res.v5 (11) two pinters: ", sol.twoSumV5([1,2,4,6,7,9],11))

    print ("Sum Three: ", sol.threeSum([1,4,7,9,2,6],11))

def printingMaxWaterContainer():
    sol = ListBundleR1()
    print("[7,1,2,3,9]")
    print("res.1: ", sol.getMaxWaterContainer([7,1,2,3,9]))
    print("res.2: ", sol.getMaxWaterContainerV2([7,1,2,3,9]))
    print("[4,8,1,2,3,9]")
    print("res.1: ", sol.getMaxWaterContainer([4,8,1,2,3,9]))
    print("res.2: ", sol.getMaxWaterContainerV2([4,8,1,2,3,9]))

def printingTrappingRainWater():
    sol = ListBundleR1()
    print("[0,1,0,2,1,0,1,3,2,1,2,1]")
    print("res.1:", sol.trapV1([0,1,0,2,1,0,1,3,2,1,2,1]))
    print("res.2:", sol.trapV2([0,1,0,2,1,0,1,3,2,1,2,1]))

    print("[4,2,0,3,2,5]")
    print("res.1:", sol.trapV1([4,2,0,3,2,5]))
    print("res.2:", sol.trapV2([4,2,0,3,2,5]))


def playasong():
    sol = ListBundleR1()
    res = sol.playAsong([4,8,1,2,3,4,3,4,7,9,1,2,3,54,6,7,8,9,7,5,3,2,4,9])

def printingContainerWithMostWater():
    sol = ListBundleR1()
    print("Container With Most Water to: [4,2,0,3,2,5]")
    res = sol.maxAreaV1([4,2,0,3,2,5])
    print("most water: ", res)
    res = sol.maxAreaV2([4,2,0,3,2,5])
    print("most water: ", res)

def printingMaximumTastinessCandyBasket():
    sol = ListBundleR1()
    print("Candy Container: [13,5,1,8,21,2]")    
    res = sol.maximumTastinessV1([13,5,1,8,21,2],3)
    print("result: ", res)

def printingBinarySearch():
    sol = ListBundleR1()
    print("Binary Search to [9]: in [-1,0,3,5,9,12]")
    res = sol.searchBinary([-1,0,3,5,9,12],9)
    print("result:", res)

def printingSumListUsingBacktracking():
    sol = ListBundleR1()
    print("Simple Sum List")
    print("Answer 1: ", sol.sumListxBacktracking([4,8,1,2,3,4,3,4,7,9,1,2,3,54,6,7,8,9,7,5,3,2,4,9]))
    print("Answer 2: ", sol.sumListxBacktracking([13,5,1,8,21,2]))
    print()
    print("Sum jumping N")
    print("Answer 1: ", sol.sumJumping([13,5,1,8,21,2],2))

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Sum II values in List")
        print("2. Max Volumn between 2 index in List")
        print("3. Trapping Rain Water")
        print("4. Container With Most Water")
        print("5. Maximum Tastiness of Candy Basket")
        print("6. Binary Search")
        print("7. Sum a List using Backtracking  ")
        print("98. play a song")
        print("99. exit()")
        x = int(input("Type option:"))
        match x:
            case 1: printingSumTwo()
            case 2: printingMaxWaterContainer()       
            case 3: printingTrappingRainWater()
            case 4: printingContainerWithMostWater()
            case 5: printingMaximumTastinessCandyBasket()
            case 6: printingBinarySearch()
            case 7: printingSumListUsingBacktracking()
            case 98: playasong()
            case 99: break

main()