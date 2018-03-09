####
#
# remove duplicates, leaving only distinct numbers in a sorted linked list.
#
# leetcode 82.
#
####

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(head):

    h0 = ListNode(0)
    h0.next = head

    dup = False
    start = h0

    while head != None:
        if head.next == None:
            if dup:
                start.next = None
            break

        if head.next.val == head.val:
            dup = True
        else:
            if dup == True:
                start.next = head.next
                dup = False
            else:
                start = head
        head = head.next

    return h0.next