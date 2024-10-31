from easy1.LinkedList1Bundle import *
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
from easy1.StringBundle import *
from easy1.BinaryBundle import * 
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


def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Evaluate Linked List Cycle")
        print("2. Intersection of Two Linked Lists")
        print("3. Remove Duplicates from Sorted List")
        print("4. Merge Lists")
        print("5. bTree Traversals")
        print("6. Same bTree")
        print("7. Symetric bTree")
        print("8. Maximus Depth in bTree")
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
            case 99: exit()

main()