####
#
# remove duplicates from sorted linked list
#
# leetcode 83.
#
####


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(head):

    li = head
    while li != None:
        if li.next == None:
            break;
        if li.next.val == li.val:
            li.next = li.next.next
        else:
            li = li.next
    return head