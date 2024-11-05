from easy1.LinkedList1Bundle import *
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
from easy1.StringBundle import *
from easy1.BinaryBundle import * 
from easy1.NumbersBundle import *
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


def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Evaluate Linked List Cycle                  21. Duplicate Zeros (LC#1089)")
        print("2. Intersection of Two Linked Lists            22. Happy Number (LC#202)")
        print("3. Remove Duplicates from Sorted List          23. Removed Linked List Elements (LC#203)")
        print("4. Merge Lists                                 24. Revert Linked List (LC#206)")
        print("5. bTree Traversals                            25. Count Complete Tree Nodes (LC#222)")
        print("6. Same bTree                                  26. Intersection Two Arrays (LC#349)")
        print("7. Symetric bTree                              27. Implement Stack using Queues (LC#225)")
        print("8. Maximus Depth in bTree                      28. Invert Binary Tree (LC#226)   ")
        print("9. Convert Sorted Array to Binary Search Tree")
        print("10. Insert List in Order to Binary Tree")
        print("11. Printing Depth Tree")
        print("12. Path Sum I, II")
        print("13. Flatten Binary Tree to Linked List")
        print("14. Generate Parentheses")
        print("15. Swap Nodes in Pairs")
        print("16. Generate Pascal Triangle I, II")
        print("17. Excel Sheet Column Title")
        print("18. Mayority Element in List")
        print("19. Excel Sheet Column Number")
        print("20. Integer to Binary Representation")
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
            case 99: exit()

main()