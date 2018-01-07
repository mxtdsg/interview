####
#
# Add 2 numbers represented by linked list in reverse order.
#
# Cracking the coding interview 2.4. Leetcode 2.
#
# Bugs Encountered: 1. Line:32 or, not and. 
#                   2. Line:40 // not /. 
#                   3. Line: 38, 41. Moved into the if statement
#
####

import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def compareNodes(self, other):
    if self == None and other == None:
        return True
    if self == None or other == None:
        return False
    if self.val != other.val:
        return False
    else:
        return compareNodes(self.next, other.next)
    


def addLinkedList(l1, l2):
    if l1 == None and l2 == None: return None
    re = first = None
    carry = 0
    while l1 != None or l2 != None:
        new_val = carry
        if l1 != None:
            new_val += l1.val
            l1 = l1.next
        if l2 != None:
            new_val += l2.val
            l2 = l2.next
        carry = new_val // 10
        new_val = new_val % 10

        if re == None:
            re = ListNode(new_val)
            first = re
        else:
            re.next = ListNode(new_val)
            re = re.next
    if carry: re.next = ListNode(1)
    return first

class TestAddLinkedList(unittest.TestCase):
    def test(self):
        # None
        self.assertEqual(addLinkedList(None, None), None)

        # No carry
        # 123 + 456 = 579
        l1 = ListNode(3)
        l1.next = ListNode(2)
        l1.next.next = ListNode(1)
        l2 = ListNode(6)
        l2.next = ListNode(5)
        l2.next.next = ListNode(4)
        l = ListNode(9)
        l.next = ListNode(7)
        l.next.next = ListNode(5)
        # self.assertEqual(addLinkedList(l1,l2), l)
        self.assertTrue(compareNodes(addLinkedList(l1,l2), l))

        # None + num
        l1 = ListNode(3)
        l1.next = ListNode(2)
        l1.next.next = ListNode(1)
        # self.assertEqual(addLinkedList(l1,None), l1)
        self.assertTrue(compareNodes(addLinkedList(l1,None), l1))

        # 342 + 485 = 827
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(8)
        l2.next.next = ListNode(4)
        l = ListNode(7)
        l.next = ListNode(2)
        l.next.next = ListNode(8)
        # self.assertEqual(addLinkedList(l1,l2), l)
        self.assertTrue(compareNodes(addLinkedList(l1,l2), l))

        # 999 + 1 = 1000
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)
        l2 = ListNode(1)
        l = ListNode(0)
        l.next = ListNode(0)
        l.next.next = ListNode(0)
        l.next.next.next = ListNode(1)
        # self.assertEqual(addLinkedList(l1,l2), l)
        self.assertTrue(compareNodes(addLinkedList(l1,l2), l))

        # 0 + 0 = 0
        l1 = ListNode(0)
        # self.assertEqual(addLinkedList(l1,l1), l1)
        self.assertTrue(compareNodes(addLinkedList(l1,l1), l1))


if __name__ == '__main__':
    unittest.main()