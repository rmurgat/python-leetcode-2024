from easy1.LinkedList1Bundle import LinkedList1Bundle

def printLinkedListCycle():
    sol = LinkedList1Bundle()
    lst = sol.createListNode([2,6,7,8,9,10])
    sol.addLinkAtListNode(lst, 10, 2)
    print("Evaluating Linked List Cycle")
    print("res=",sol.hasCycle(lst))

def printIntersection2LinkedLists()
    sol = LinkedList1Bundle()
    la = sol.createListNode([4,1,8,4,5])
    lb = sol.createListNode([5,6,1,8,4,5])
    lst = sol.getIntersectionNode()
    


def main():
    while True:
        print("\n[ MAIN MENU ] ")
        print("1. Evaluate Linked List Cycle")
        print("2. Intersection of Two Linked Lists")
        print("")
        print("99. to Exit")
        x = int(input("Type option:"))
        match x:
            case 1: printLinkedListCycle()
            case 2: print

        


main()