from typing import Optional

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TwoNumbers:

    def num2ListNode(num: str) ->ListNode:
        res = None
        for car in num:
            res = ListNode(car,res)
        return res

    def printListNode(listNode: ListNode):
        while True: 
            print (listNode.val, end=", ")
            if listNode.next: listNode = listNode.next 
            else: break
        

    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        if l2 is None: return l1
        head = ListNode(0)
        node = head
        remain = 0
        while l1 or l2:
            if l1: 
                node.val+=int(l1.val)
                l1 = l1.next
            if l2: 
                node.val+=int(l2.val)
                l2 = l2.next
            if node.val>9: 
                remain=1
                node.val-=10
            else:
                remain=0
            if remain or l1 or l2:
                node.next = ListNode(remain)
                node = node.next
        return head
