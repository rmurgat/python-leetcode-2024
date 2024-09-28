from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList1Bundle:
    def createListNode(self, lst: list)-> Optional[ListNode]:
        if len(lst)==0: return None
        head = ListNode()
        r = head
        for i in range(0, len(lst)):
            r.val = lst[i]
            if i < len(lst)-1:
                r.next = ListNode()
                r = r.next
        return head
    
    def addListNodeAtEnd(self, lst: Optional[ListNode], val):
        if lst is None: 
            lst = ListNode(val)
        else:
            while lst.next : lst = lst.next
            lst.next = ListNode(val)

    def addLinkAtListNode(self, lst:Optional[ListNode], val1, val2):
        nval2 = None
        p = lst
        while(p):
            if p.val == val2: 
                nval2 = p
                break
            p = p.next

        p = lst            
        if nval2:
            while(p):
                if p.val == val1: 
                    p.next = nval2
                    break
                p = p.next

    def convertListNode2String(self, llst: ListNode):
        ll = llst
        r = ""
        while ll:
            r += str(ll.val)
            if ll.next: r +=", " 
            ll = ll.next
        return r

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1
        r = ListNode(0)
        head = r

        while list1 and list2:
            if list1.val < list2.val:
                r.val = list1.val
                list1 = list1.next
            else:
                r.val = list2.val
                list2 = list2.next
            if list1 and list2:
                r.next = ListNode(0)
                r = r.next
        if list1 is None: r.next = list2
        if list2 is None: r.next = list1
        return head
            
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        p = head
        bcycle = False
        while p:
            found = p in nodes
            if found: return True
            else:
                nodes.append(p)
            p = p.next
        return bcycle
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        return None