from easy1.LinkedList1Bundle import LinkedList1Bundle
from easy1.ListBundle import ListBundle
from easy1.BTreeBundle1 import *
import math

def printLinkedListCycle():
    sol = LinkedList1Bundle()
    lst = sol.createListNode([2,6,7,8,9,10])
    sol.addLinkAtListNode(lst, 10, 2)
    print("Evaluating Linked List Cycle")
    print("res=",sol.hasCycle(lst))

def printIntersection2LinkedLists():
    sol = LinkedList1Bundle()
    la = sol.createListNode([4,1,8,4,5])
    lb = sol.createListNode([5,6,1,8,4,5])
    lst = sol.getIntersectionNode()
    
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

def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Evaluate Linked List Cycle")
        print("2. Intersection of Two Linked Lists (pending)")
        print("3. Remove Duplicates from Sorted List")
        print("4. Merge Lists")
        print("5. bTree Traversals")
        print("6. Same bTree")
        print("7. Symetric bTree")
        print("8. Maximus Depth in bTree")
        print("9. Convert Sorted Array to Binary Search Tree")
        print("10. Insert List in Order to Binary Tree")
        print("11. Printing Depth Tree")
        print("")
        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printLinkedListCycle()
            case 2: print("Intersection of Two Linked Lists (pending)")
            case 3: printRemoveDuplicatesFromSortedList()
            case 4: printListMerged()
            case 5: printBTreeInOrderTraversal()
            case 6: printBTreeSameTree()
            case 7: printBTreeIsSymetric()
            case 8: printBTreeMaxDepth()
            case 9: convertSortedList2BSTBalanced()
            case 10: insertingInOrderBinaryTree()
            case 11: printDepthTree()

main()