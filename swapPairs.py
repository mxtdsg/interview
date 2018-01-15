####
#
# Swap every pairs in a linked list.
#
# leetcode 24
#
####

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None: return head

    n1 = ListNode(0)
    n1.next = head

    re = n1

    while True:        
        n2 = n1.next
        n3 = n2.next
        if n3 == None:
            break
        n4 = n3.next

        n1.next = n3
        n3.next = n2
        n2.next = n4

        if n4 == None:
            break

        n1 = n1.next.next

    return re.next