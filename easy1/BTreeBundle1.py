from typing import List, Optional


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

    def prettyTree(self, root: TreeNode, last=True, header='', side=''):
       elbow = "└──"
       pipe = "│  "
       tee = "├──"
       blank = "   "
       if root is None: return
       print(header + (elbow if last else tee) + str(root.val)+("" if side=='' else "-"+side))
       if root.left: self.prettyTree(root=root.left, last=False if root.right else True, header=header + (blank if last else pipe),side="l" )
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



                