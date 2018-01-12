####
#
# remove Nth node from the end of the linked list.
#
# leetcode 19
#
####

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    #find n+1th node from the last
    p1 = p2 = head
    for i in range(n):
        p2 = p2.next
    # deleting the first
    if p2 == None:
        return head.next
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    p1.next = p1.next.next
    return head