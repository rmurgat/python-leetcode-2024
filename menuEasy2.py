from easy1.LinkedList1Bundle import *
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
from easy1.StringBundle import *
from easy1.BinaryBundle import * 
from easy1.NumbersBundle import *
from easy1.MatrixBundle import *
from easy1.MyStack import *

import math

def printLinkedListCycle():
    sol = LinkedList1Bundle()
    lst = sol.createListNode([2,6,7,8,9,10])
    sol.addLinkAtListNode(lst, 10, 2)
    print("Evaluating Linked List Cycle")
    print("res=",sol.hasCycle(lst))

def printIntersection2LinkedLists():
    sol = LinkedList1Bundle()
    la = ListNode(1)
    la.next = ListNode(9)
    la = la.next
    la.next = ListNode(1)
    la = la.next 
    intersec = la.next = ListNode(2)
    la = la.next
    la.next = ListNode(4)

    lb = ListNode(3)
    lb.next = intersec

    res = sol.getIntersectionNode(la, lb)
    print ("Node Intersection: ", res.val)
    print ("rest list: [ ", end ="")
    while res:
        print(res.val,", ", end="")
        res = res.next
    print ("]")
    
def printRemoveDuplicatesFromSortedList():
    sol = LinkedList1Bundle()
    la = sol.createListNode([1,1,2,3,3])
    res = sol.deleteDuplicates(la)
    print("result: ", sol.convertListNode2String(res))

def printListMerged():
    sol = ListBundle()
    nums1 = [2,0]
    nums2 = [1]
    sol.merge(nums1,1,nums2,1)
    print("result:", nums1)

def printBTreeInOrderTraversal():
    sol = BTreeBundle1()
    root = TreeNode(12)
    sol.insertBST(root,5)
    sol.insertBST(root,7)
    sol.insertBST(root,20)
    sol.insertBST(root,13)
    sol.insertBST(root,14)
    sol.insertBST(root,6)
    sol.prettyTree(root)

    print("bTree inOrder-traversal:", sol.inorderTraversal(root))
    print("bTree preOrder-traversal:", sol.preorderTraversal(root))
    print("bTree postOrder-Traversal:", sol.postorderTraversal(root))

def printBTreeSameTree():
    sol = BTreeBundle1()
    bt1 = TreeNode(12)
    sol.insertBST(bt1,5)
    sol.insertBST(bt1,7)
    sol.insertBST(bt1,20)
    sol.insertBST(bt1,13)
    sol.insertBST(bt1,14)
    sol.insertBST(bt1,6)

    bt2 = TreeNode(12)
    sol.insertBST(bt2,5)
    sol.insertBST(bt2,7)
    sol.insertBST(bt2,20)
    sol.insertBST(bt2,13)
    sol.insertBST(bt2,14)
    sol.insertBST(bt2,6)

    sol.prettyTree(bt1)
    sol.prettyTree(bt2)
    res = sol.isSameTree(bt1,bt2)
    print("Same Trees: ", res)

def printBTreeIsSymetric():
    sol = BTreeBundle1()
    bt1 = TreeNode(1)
    bt1.left = TreeNode(2)
    bt1.left.left = TreeNode(3)
    bt1.left.right = TreeNode(4)
    bt1.right = TreeNode(2)
    bt1.right.right = TreeNode(3)
    bt1.right.left = TreeNode(4)
    print ("Is BTree Symetric?: ", sol.isSymmetric(bt1))
    sol.prettyTree(bt1)

def printBTreeMaxDepth():
    sol = BTreeBundle1()
    bt1 = TreeNode(1)
    bt1.left = TreeNode(2)
    bt1.left.left = TreeNode(3)
    bt1.left.right = TreeNode(4)
    bt1.right = TreeNode(2)
    bt1.right.right = TreeNode(3)
    bt1.right.left = TreeNode(4)
    bt1.right.left.left = TreeNode(100)
    sol.prettyTree(bt1)    
    print ("Max bTree: ", sol.maxDepth(bt1))


def convertSortedList2BSTBalanced():
    sol = BTreeBundle1()
    bt1 = TreeNode(1)
    bt1.left = TreeNode(2)
    bt1.left.left = TreeNode(3)
    bt1.left.left.left = TreeNode(4)
    bt1.right = TreeNode(2)
    bt1.right.right = TreeNode(3)
    bt1.right.right.right = TreeNode(4)

    sol.prettyTree(bt1)  
    print("Is Balanced: ", sol.isBalanced(bt1))  

def insertingInOrderBinaryTree():
    sol = BTreeBundle1()
    lst = [3,9,20,None,None,15,7]
    root = sol.insertInOrder(lst)
    sol.prettyTree(root)

def printDepthTree():
    sol = BTreeBundle1()    
    lst = [2,None,3,None,4,None,5,None,6]
    root = sol.insertInOrder(lst)
    sol.prettyTree(root)
    print("min Depth:", sol.minDepth(root))
    print("max Depth:", sol.maxDepth(root))

def printPathSum():
    sol = BTreeBundle1()    
    root = sol.insertInOrder([5,4,8,11,None,13,4,7,2,None,None,None,1])
    root2 = sol.insertInOrder([5,4,8,11,None,13,4,7,2,None,None,5,1])
    print("root tree")
    sol.prettyTree(root)
    print("Path Sum I", 22, " : ", sol.hasPathSum(root, 22))
    print("root2 tree")
    sol.prettyTree(root2)
    print("Path Sum II", 22, " : ", sol.pathSumII(root2, 22))

def printFlattenBinaryTree2LinkedList():
    sol = BTreeBundle1() 
    root = sol.insertInOrder([1,2,None,3,4,5])
    print("root Tree (original)")
    sol.prettyTree(root)    
    sol.flatten(root)
    print("root Tree (flatted)")
    sol.printPrettyTreeRight(root)

def printGenerateParentheses():
    sol = BTreeBundle1()  
    res = sol.generateParenthesis(3)
    print("res: ", res)

def printSwapNodesInPairs():
    sol = LinkedList1Bundle()
    head = sol.createListNode([1,2,3,4,5,6,7])
    head = sol.swapPairs(head)
    print("res: ", sol.convertListNode2String(head))

def printPascalTriangle():
    sol = ListBundle()
    print("printPascalTriangle.I()")    
    print("result:",  sol.generatePascalTriangle(5))
    print("printPascalTriangle.II()")    
    print("result:",  sol.getRowPascalTriangle(4))

def printExcelColumnTitle():
    sol = StringBundle()
    print("ASCII: ", sol.convertToTitle(701))

def printMayorityelement():
    sol = ListBundle()
    print("res: ",sol.majorityElement([2,2,1,1,1,2,2]))

def printExcelSheetColumnNumber():
    sol = StringBundle()
    print("res: ", sol.titleToNumber("ZY") )    

def printReversingBinary():
    sol = BinaryBundle()

    print("res (20365): ", sol.InvertBinaryDecimal(20365))
    print("verify (20365): ", format(20365,'b'))

def printDuplicatingZeros():
    sol = ListBundle()
    arr = [1,0,2,3,0,4,5,0]
    sol.duplicateZeros1(arr)
    print("Answer #1: (low performance) ", arr)
    arr = [1,0,2,3,0,4,5,0]
    sol.duplicateZeros2(arr)    
    print("Answer #1: (optimized)", arr)

def printHappyNumber():
    lib = NumbersBundle()
    print(" The Happy Number ")
    print("Answer #1 ", lib.isHappy(19))
    print("Answer #1 ", lib.isHappy(2))

def printRemoveLinkedListElement():
    lib = LinkedList1Bundle()
    print (" Removed Linked List Element ")
    head = lib.createListNode([1,2,6,3,4,5,6])
    print ("Answer # 1: ", lib.convertListNode2String(lib.removeElements(head,6)))
    head = lib.createListNode([7,7,7,7,1])
    print ("Answer # 2: ", lib.convertListNode2String(lib.removeElements(head,7)))
    head = lib.createListNode([1,2,2,1])
    print ("Answer # 3: ", lib.convertListNode2String(lib.removeElements(head,2)))    

def printRevertLinkedList():
    lib = LinkedList1Bundle()
    print (" Reverting Linked List Elements ")
    print ("Answer # 1: ", lib.convertListNode2String(lib.reverseList(lib.createListNode([1,2,3,4,5]))))
    print ("Answer # 1: ", lib.convertListNode2String(lib.reverseList(lib.createListNode([1,2]))))
    print ("Answer # 1: ", lib.convertListNode2String(lib.reverseList(lib.createListNode([]))))

def printCountCompleteTreeNodes():
    lib = BTreeBundle1()
    head = lib.insertInOrder([1,2,3,4,5,6])
    print ("print bTree: ", lib.prettyTree(head))
    print ("answer #1: ", lib.countNodes(head))

def printIntersectionTwoArrays():
    lib = ListBundle()
    print ("Print Intersection() in Two Arrays")
    print ("Answer #1: ", lib.intersection1([1,2,2,1],[2,2]))
    print ("Answer #1: ", lib.intersection2([1,2,2,1],[2,2]))
    print ("Answer #1: ", lib.intersection3([1,2,2,1],[2,2]))
    print ()
    print ("Answer #1: ", lib.intersection1([4,9,5],[9,4,9,8,4]))
    print ("Answer #1: ", lib.intersection2([4,9,5],[9,4,9,8,4]))
    print ("Answer #1: ", lib.intersection3([4,9,5],[9,4,9,8,4]))    
    print ()
    print ("Answer II #1: ", lib.intersectII_1([4,9,5],[9,4,9,8,4]))
    print ("Answer II #2: ", lib.intersectII_1([1,2,2,1],[2]))
    print ()    
    print ("Answer II #1: ", lib.intersectII_2([4,9,5],[9,4,9,8,4]))
    print ("Answer II #2: ", lib.intersectII_2([1,2,2,1],[2]))
    
def printImplementingStackUsingQueues():
    lib = MyStack()
    lib.push("MyStack")
    lib.push("push")
    lib.push("push")
    lib.push("top")
    lib.push("pop")
    lib.push("empty")

    print(" pop: ", lib.pop())
    print(" top: ", lib.top())
    print(" empty: ", lib.empty())

def printInvertBinaryTree():
    lib = BTreeBundle1()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print("original tree:")
    lib.prettyTree(root)
    print("inverted tree:")
    inverted = lib.invertTree(root)
    lib.prettyTree(inverted)

def printThreeSumClosest():
    lib = ListBundle()
    print ("Answer #1", lib.threeSumClosest_1([-100,-98,-2,-1], -101))
    print ("Answer #2", lib.threeSumClosest_1([-1,2,1,-4],1))
    print ("Answer #3", lib.threeSumClosest_1([0,1,2],3))
    print()
    print ("Answer #1", lib.threeSumClosest_2([-100,-98,-2,-1], -101))
    print ("Answer #2", lib.threeSumClosest_2([-1,2,1,-4],1))
    print ("Answer #3", lib.threeSumClosest_2([0,1,2],3))    
    print()
    print ("Answer #1 (passed)", lib.threeSumClosest_3([-100,-98,-2,-1], -101))
    print ("Answer #2 (passed)", lib.threeSumClosest_3([-1,2,1,-4],1))
    print ("Answer #3 (passed)", lib.threeSumClosest_3([0,1,2],3))    

def printLetterCombinationPhone():
    lib = ListBundle()
    print ("Answer #1 (passed)", lib.letterCombinations_1("23"))
    print ("Answer #2 (passed)", lib.letterCombinations_1("2"))
    print ("Answer #3 (passed)", lib.letterCombinations_1("197"))
    print ("Answer #4 (passed)", lib.letterCombinations_1(""))

def printSummaryRanges():
    lib = ListBundle()
    print ("Answer #1: (passed)", lib.summaryRanges([0,1,2,4,5,7]))
    print ("Answer #2: (passed)", lib.summaryRanges([0,2,3,4,6,8,9]))

def printIsPowerOfTwo():
    lib = NumbersBundle()
    print ("Answer #1: (16) ", lib.isPowerOfTwo_1(16))
    print ("Answer #2: (17) ", lib.isPowerOfTwo_1(17))
    print()
    print ("Answer #1: (16) ", lib.isPowerOfTwo_2(16))
    print ("Answer #2: (17) ", lib.isPowerOfTwo_2(17))

def printIsPalindromeLinkedList():
    lib = LinkedList1Bundle()
    head = lib.createListNode([1,2,2,1])
    print ("original linkedlist #1:", lib.convertListNode2String(head))
    print ("is palindrome #1: ", lib.isPalindrome(head))

    head = lib.createListNode([1,2])
    print ("original linkedlist #2:", lib.convertListNode2String(head))
    print ("is palindrome #2: ", lib.isPalindrome(head))

    head = lib.createListNode([1,0,0])
    print ("original linkedlist #2:", lib.convertListNode2String(head))
    print ("is palindrome #2: ", lib.isPalindrome(head))

    head = lib.createListNode([1,0,1])
    print ("original linkedlist #2:", lib.convertListNode2String(head))
    print ("is palindrome #2: ", lib.isPalindrome(head))

def printLowestCommonAncestorBTS():
    lib = BTreeBundle1()
    head = TreeNode(6)
    head.left = TreeNode(2)
    head.right = TreeNode(8)
    ans = lib.lowestCommonAncestorBST_1(head, head.left, head.right)
    ans2 = lib.lowestCommonAncestorBST_2(head, head.left, head.right)
    print ("answer #1", ans.val)
    print ("answer #2", ans2.val)

def printLowestCommonAncestorBT():
    lib = BTreeBundle1()
    head = TreeNode(6)
    head.left = TreeNode(2)
    head.right = TreeNode(8)
    ans = lib.lowestCommonAncestorBT_1(head, head.left, head.right)
    print ("answer #1 : ", ans.val)

def printDeleteCurrentNodeInLinkedList():
    lib = LinkedList1Bundle()
    head = lib.createListNode([1,2,3,4,5,6,7,8,9,10,11,12])
    todelete = lib.findNode(head, 8)
    lib.deleteNode(todelete)
    print ("answer #1: ", lib.convertListNode2String(head))

def printProductoOfArrayExceptSelf():
    lib = ListBundle()
    ans = lib.productExceptSelf_1([1,2,3,4])
    print("Answer #1: ",  ans)    
    ans = lib.productExceptSelf_1([-1,1,0,-3,3])
    print("Answer #2: ",  ans)
    print()
    ans = lib.productExceptSelf_2([1,2,3,4])
    print("Answer #3: ",  ans)    
    ans = lib.productExceptSelf_2([-1,1,0,-3,3])
    print("Answer #4: ",  ans)

def print4Sum():

    lib = ListBundle()
    
    print("Answer #1: ", lib.fourSum_1([1,0,-1,0,-2,2],0))
    print("Answer #2: ", lib.fourSum_1([2,2,2,2,2],8))
    print("Answer #3: ", lib.fourSum_1([-5,5,4,-3,0,0,4,-2],4))
    print("Answer #4: ", lib.fourSum_1([-3,-1,0,2,4,5],2))

def printNextPermutation():
    lib = ListBundle()
    
    print("Answer #1: ", lib.nextPermutation_1([1,2,3]))
    print()
    print("Answer #2: ", lib.nextPermutation_2([1,2,3]))
    print()
    print("Answer #3: ", lib.nextPermutation_2([3,2,1]))

def printSeachInRotatedArray():
    lib = ListBundle()
    print("Answer #1: ", lib.searchInRotated([4,5,6,7,0,1,2], 0))
    print("Answer #2: ", lib.searchInRotated([4,5,6,7,0,1,2], 3))
    print("Answer #3: ", lib.searchInRotated([1], 0))
    print("Answer #3: ", lib.searchInRotated([5,1,3], 5))

def printFind1stAndLastPositioninArray():
    lib = ListBundle()
    print("Answer #1: ", lib.searchRange([5,7,7,8,8,10], 8))
    print("Answer #2: ", lib.searchRange([5,7,7,8,8,10], 6))

def printIsValidSudoku():
    lib = MatrixBundle()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    print("Answer #1:", lib.isValidSudoku(board))

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]    
    
    print("Answer #2:", lib.isValidSudoku(board))
    board = [[".",".",".",".","5",".",".","1","."]
            ,[".","4",".","3",".",".",".",".","."]
            ,[".",".",".",".",".","3",".",".","1"]
            ,["8",".",".",".",".",".",".","2","."]
            ,[".",".","2",".","7",".",".",".","."]
            ,[".","1","5",".",".",".",".",".","."]
            ,[".",".",".",".",".","2",".",".","."]
            ,[".","2",".","9",".",".",".",".","."]
            ,[".",".","4",".",".",".",".",".","."]]
    print("Answer #3:", lib.isValidSudoku(board))

def printSudokuSolver():
    lib = MatrixBundle()    
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print("[solving...original]")     
    #lib.printPrint(board)
    #print("[solving...brute force]") 
    #lib.solveSudoku_1(board)
    lib.printPrint(board)
    print("[solving...optimized]") 
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    lib.solveSudoku_2(board)
    lib.printPrint(board)
    print("[solving #2...optimized]")     
    board = [[".",".","9","7","4","8",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","2",".","1",".","9",".",".","."],
             [".",".","7",".",".",".","2","4","."],
             [".","6","4",".","1",".","5","9","."],
             [".","9","8",".",".",".","3",".","."],
             [".",".",".","8",".","3",".","2","."],
             [".",".",".",".",".",".",".",".","6"],
             [".",".",".","2","7","5","9",".","."]]
    lib.solveSudoku_2(board)
    lib.printPrint(board)

def printRemoveNthNodeFromEndofList():
    lib = LinkedList1Bundle()
    head = lib.createListNode([1,2,3,4,5])
    head = lib.removeNthFromEnd(head, 1)
    print("Answer #1: ", lib.convertListNode2String(head))

def printDivideTwoIntegers():
    lib = NumbersBundle()
    print("Answer #1: ", lib.divide_1(10, 3))
    print("Answer #2: ", lib.divide_1(100, 35))
    print("Answer #3: ", lib.divide_1(3500, 3000))
    print("Answer #4: ", lib.divide_1(7, -3))
    print("Answer #5: ", lib.divide_1(0, 1))
    print("Answer #6: ", lib.divide_1(-1, 1))
    print("Answer #7: ", lib.divide_1(-2147483648,-1))

def printCountAndSay():
    lib = StringBundle()
    print("Answer #1: ", lib.countAndSay(1))
    print("Answer #2: ", lib.countAndSay(4))

def printMultiplyStrings():
    lib = StringBundle()
    print("Answer #1: ", lib.multiply("2", "3"))   #Output : 6
    print("Answer #2: ", lib.multiply("456","123"))   #Output : 56088
    print("Answer #3: ", lib.multiply("4154", "51454"))   #Output : 213739916
    print("Answer #4: ", lib.multiply("654154154151454545415415454", "63516561563156316545145146514654"))   #Output : 41549622603955309777243716069997997007620439937711509062916

def printJumpGame():
    lib = ListBundle()
    print("Answer #1:", lib.canJump_1([1,2])) 
    print("Answer #2:", lib.canJump_1([2,0]))
    print("Answer #3:", lib.canJump_1([2,3,1,1,4]))
    print("Answer #4:", lib.canJump_1([3,2,1,0,4]))
    print("Answer #5:", lib.canJump_1([2,0,0]))
    print()
    #print("Answer #1:", lib.canJump_2([1,2])) 
    #print("Answer #2:", lib.canJump_2([2,0]))
    #print("Answer #6:", lib.canJump_2([2,3,1,1,4]))
    #print("Answer #7:", lib.canJump_2([3,2,1,0,4]))
    #print("Answer #5:", lib.canJump_2([2,0,0]))
    large1 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print("Answer #5:", lib.canJump_2(large1))

def printMergeIntervals():
    lib = ListBundle()
    print("Answer #1: ", lib.merge([[1,3],[2,6],[8,10],[15,18]]))
    print("Answer #2: ", lib.merge([[1,4],[4,5]]))
    print("Answer #3: ", lib.merge([[1,4],[2,3]]))
    print("Answer #4: ", lib.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))

def printCombinations():
    lib = ListBundle()
    print("Combinations #1:", lib.combine_1(4,2), " (backtracking)")
    print("combinations #2:", lib.combine_2(4,2), " (backtracking)")

def printPermutations():
    lib = ListBundle()
    print("Permutations #1:", lib.permuteRaw_1(2,2), " (backtracking)")
    print("Permutations #1:", lib.permuteRaw_1(4,2), " (backtracking)")
    print("Permutations #1:", lib.permuteRaw_1(3,3), " (backtracking)")
    print()
    print("Permutations #2:", lib.permute([1,2,3]))
    print("Permutations #2:", lib.permute([0,1]))
    print("Permutations #2:", lib.permute([1]))

def printCombinationSum():
    lib = ListBundle()
    print ("Conbination #1: ", lib.combinationSum([2,3,6,7],7))
    print ("Conbination #1: ", lib.combinationSum([2,3,5],8))

def printCombinationSumII():
    lib = ListBundle()
    print ("Answer #1 (no passing):", lib.combinationSum2_1([10,1,2,7,6,1,5],8))
    print ("Answer #1 (no passing):", lib.combinationSum2_2([10,1,2,7,6,1,5],8))
    

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Evaluate Linked List Cycle                  21. Duplicate Zeros (LC#1089)                 41. Find first,last idx in Array (LC#34)")
        print("2. Intersection of Two Linked Lists            22. Happy Number (LC#202)                     42. Is Valida Sudoku Matrix (LC#36) ")
        print("3. Remove Duplicates from Sorted List          23. Removed Linked List Elements (LC#203)     43. Matrix Sudoku Solver (LC#37) SOLVED")
        print("4. Merge Lists                                 24. Revert Linked List (LC#206)               44. Remove Nth Node from End of List (LC#19)")
        print("5. bTree Traversals                            25. Count Complete Tree Nodes (LC#222)        45. Divide Two Integers (LC#29)")
        print("6. Same bTree                                  26. Intersection Two Arrays (LC#349)          46. Count and Say (LC#38)")
        print("7. Symetric bTree                              27. Implement Stack using Queues (LC#225)     47. Multiply String [LC#43] [to do faster]")
        print("8. Maximus Depth in bTree                      28. Invert Binary Tree (LC#226)               48. Jump Game (LC#55)")
        print("9. Convert Sorted Array to Binary Search Tree  29. Three Sum Closest (LC#16)                 49. Merge Intervals (LC#56)")
        print("10. Insert List in Order to Binary Tree        30. Letter Combinatons of a Phone Number      50. Combinations (LC#77)")
        print("11. Printing Depth Tree                        31. Summary Ranges (LC#228)                   51. Permutations (LC#46)")
        print("12. Path Sum I, II                             32. Is power of Two (LC#231)                  52. Combination Sum (LC#39)")
        print("13. Flatten Binary Tree to Linked List         33. Is Palindrome Linked List (LC#234)        53. Combination Sum II (LC#40)")
        print("14. Generate Parentheses                       34. Lowest Common Ancestor of a BST (LC#235)")
        print("15. Swap Nodes in Pairs                        35. Lowest Common Ancestor of a BT (LC#236)")
        print("16. Generate Pascal Triangle I, II             36. Delete current Node @linkedList (LC#237)")
        print("17. Excel Sheet Column Title                   37. Product of Array Except Self (LC#238)")
        print("18. Mayority Element in List                   38. 4 Sum (LC#18)")
        print("19. Excel Sheet Column Number                  39. Next Permutations (LC#31) ERROR!")
        print("20. Integer to Binary Representation           40. Search in Rotated Sorted Array (LC#33)")
        print("")
        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printLinkedListCycle()
            case 2: printIntersection2LinkedLists()
            case 3: printRemoveDuplicatesFromSortedList()
            case 4: printListMerged()
            case 5: printBTreeInOrderTraversal()
            case 6: printBTreeSameTree()
            case 7: printBTreeIsSymetric()
            case 8: printBTreeMaxDepth()
            case 9: convertSortedList2BSTBalanced()
            case 10: insertingInOrderBinaryTree()
            case 11: printDepthTree()
            case 12: printPathSum()
            case 13: printFlattenBinaryTree2LinkedList()
            case 14: printGenerateParentheses()
            case 15: printSwapNodesInPairs()
            case 16: printPascalTriangle()
            case 17: printExcelColumnTitle() 
            case 18: printMayorityelement()
            case 19: printExcelSheetColumnNumber()
            case 20: printReversingBinary()
            case 21: printDuplicatingZeros()
            case 22: printHappyNumber()
            case 23: printRemoveLinkedListElement()
            case 24: printRevertLinkedList()
            case 25: printCountCompleteTreeNodes()
            case 26: printIntersectionTwoArrays()
            case 27: printImplementingStackUsingQueues()
            case 28: printInvertBinaryTree()
            case 29: printThreeSumClosest()
            case 30: printLetterCombinationPhone()
            case 31: printSummaryRanges()
            case 32: printIsPowerOfTwo()
            case 33: printIsPalindromeLinkedList()
            case 34: printLowestCommonAncestorBTS()
            case 35: printLowestCommonAncestorBT()
            case 36: printDeleteCurrentNodeInLinkedList()
            case 37: printProductoOfArrayExceptSelf()
            case 38: print4Sum()
            case 39: printNextPermutation()
            case 40: printSeachInRotatedArray()
            case 41: printFind1stAndLastPositioninArray()
            case 42: printIsValidSudoku()
            case 43: printSudokuSolver()
            case 44: printRemoveNthNodeFromEndofList()
            case 45: printDivideTwoIntegers()
            case 46: printCountAndSay()
            case 47: printMultiplyStrings()
            case 48: printJumpGame()
            case 49: printMergeIntervals()
            case 50: printCombinations()
            case 51: printPermutations()
            case 52: printCombinationSum()
            case 53: printCombinationSumII()
            case 99: exit()

main()