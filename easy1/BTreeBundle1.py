from typing import List, Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BTreeBundle1:

    def __init__(self) -> None:
        pass

    def insertBST(self, root: TreeNode, val: int):
        if root is None:
            root = TreeNode(val)
            return
        
        if val < root.val:
            if root.left:
                self.insertBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertBST(root.right, val)
            else:
                root.right = TreeNode(val)

    def insertInOrder(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        it = iter(nums)
        root = TreeNode(next(it))
        q = [root]
        for node in q:
            val = next(it, None)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(it, None)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
        return root

    def prettyTree(self, root: TreeNode, last=True, header='', side=''):
       elbow = "└──"
       pipe = "│  "
       tee = "├──"
       blank = "   "
       if root is None: return
       print(header + (elbow if last else tee) + str(root.val)+("" if side=='' else "-"+side))
       if root.left: self.prettyTree(root=root.left, last=False if root.right else True, header=header + (blank if last else pipe),side="l" )
       if root.right: self.prettyTree(root=root.right, last=True, header=header + (blank if last else pipe), side="r")    

    def printPrettyTreeRight(self, root: TreeNode, last=True, header='', side=''):
       elbow = "└──"
       pipe = "│  "
       tee = "├──"
       blank = "   "
       if root is None: return
       print(header + (elbow if last else tee) + str(root.val)+("" if side=='' else "-"+side))
       if root.right: self.prettyTree(root=root.right, last=True, header=header + (blank if last else pipe), side="r")    

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None: return res
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res = res + self.inorderTraversal(root.right)
        return res
    
    def preorderTraversal(self, root: Optional[TreeNode])->List[int]:
        res = []
        if root is None: return res
        res.append(root.val)
        res = res + self.preorderTraversal(root.left)
        res = res + self.preorderTraversal(root.right)
        return res
    
    def postorderTraversal(self, root: Optional[TreeNode])->List[int]:
        res=[]
        if root is None: return res
        res = self.postorderTraversal(root.left)
        res = res + self.postorderTraversal(root.right)
        res.append(root.val)
        return res
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val!=q.val: return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(n, m) -> bool:
            if not n and not m: return True
            if not n or not m: return False
            return n.val==m.val and isMirror(n.left, m.right) and isMirror(n.right, m.left)
        return isMirror(root.left, root.right)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthNode(node, depth) -> int:
            if not node: 
                return depth
            return max(maxDepthNode(node.left, depth + 1), maxDepthNode(node.right, depth + 1))
        return maxDepthNode(root,0)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(lst:List[int]) -> Optional[TreeNode]:
            if not lst: return None
            last=len(lst)
            mid = math.floor(last/2)
            res = TreeNode(lst[mid])
            res.left = divide(lst[0:mid])
            res.right = divide(lst[mid+1:last])
            return res
        res = divide(nums)
        return res
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root: Optional[TreeNode]) -> int:
            if not root: return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            if left < 0 or right < 0: return -1
            if abs(left - right) > 1: return -1
            return max(left, right) + 1
        depth=getDepth(root)
        print("depth:",depth)
        return depth >= 0

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        d = []
        def getDepths(tree: Optional[TreeNode], depth: int, d: List[int]):
            if not tree:
                return
            if not tree.left and not tree.right: 
                d.append(depth)
                return
            getDepths(tree.left, depth+1, d)
            getDepths(tree.right, depth+1, d)
        getDepths(root, 1, d)
        return min(d) 
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:  return []        
        self.pool = []
        def getPathSum(root: Optional[TreeNode], tmp: List[int], target: int):
            tmp.append(root.val)
            if not root.left and not root.right:
                if sum(tmp) == target:
                    self.pool.append(tmp.copy())
            if root.left:
                getPathSum(root.left, tmp, target)
            if root.right:
                getPathSum(root.right, tmp, target)
            tmp.pop()
        getPathSum(root, [], targetSum)
        return len(self.pool)>0

    def pathSumII(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:  return []        
        self.pool = []
        def getPathSum(root: Optional[TreeNode], tmp: List[int], target: int):
            tmp.append(root.val)
            if not root.left and not root.right:
                print (tmp)
                if sum(tmp) == target:
                    self.pool.append(tmp.copy())
            if root.left:
                getPathSum(root.left, tmp, target)
            if root.right:
                getPathSum(root.right, tmp, target)
            tmp.pop()
        getPathSum(root, [], targetSum)
        return self.pool
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return

        def preOrder(root:TreeNode):
            if not root: return
            if root.left: 
                tmp = root.right
                root.right = root.left
                tmp1 = root.right
                while tmp1.right:
                    tmp1 = tmp1.right
                tmp1.right = tmp
                root.left = None
            preOrder(root.right)            

        preOrder(root)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open1, close1):
            print("".join(stack))
            if open1 == close1 == n:
                res.append("".join(stack))
                return
            if open1<n:
                stack.append("(")
                backtrack(open1 + 1, close1)
                stack.pop()
            if close1 < open1:
                stack.append(")")
                backtrack(open1, close1 + 1)
                stack.pop()
        backtrack(0,0)
        return res
    

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 1 
        total = total + self.countNodes(root.left)
        total = total + self.countNodes(root.right)

        return total
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        tmpleft = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmpleft)
        return root

