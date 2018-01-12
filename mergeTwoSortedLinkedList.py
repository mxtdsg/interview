####
#
# merge two sorted linked list
#
# leetcode 21
#
####

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    re = finalre = ListNode(0)
    while not (l1 == None or l2 == None):
        if l1.val < l2.val:
            re.next = l1
            l1 = l1.next
        else:
            re.next = l2
            l2 = l2.next
        re = re.next
    if l1 == None and l2 == None:
        return finalre.next
    if l1 == None:
        re.next = l2
    if l2 == None:
        re.next = l1
    return finalre.next