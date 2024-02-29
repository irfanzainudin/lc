from typing import Optional
import math


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def construct_number(self, ll: Optional[ListNode]) -> int:
        place_value = 0
        actual_number = 0
        # MISTAKE: Python does not need the type for declaration
        # ListNode cur = l1
        cur = ll
        while cur.next != None:
            actual_number = actual_number + (cur.val * (10**place_value))

            # proceeds to the next ListNode
            cur = cur.next
            place_value += 1
        actual_number = actual_number + (cur.val * (10**place_value))

        return actual_number

    def construct_ll(self, num: int) -> Optional[ListNode]:
        digits = len(str(num))
        str_num = str(num)

        genesis = ListNode(val=int(str_num[digits - 1]))
        for num in str_num[::-1]:
            pass

        return genesis

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # construct the actual number first from the linked-list
        nu1 = self.construct_number(l1)
        nu2 = self.construct_number(l2)
        # add them
        sum = nu1 + nu2
        # convert them back into a linked-list
        l3 = self.construct_ll(sum)
        print("self.construct_number(l3):", self.construct_number(l3))
        return l3


# l1 = [2,4,3], l2 = [5,6,4]
n1 = ListNode(val=2)
n2 = ListNode(val=4)
n3 = ListNode(val=3)
n4 = ListNode(val=5)
n5 = ListNode(val=6)
n6 = ListNode(val=4)

n1.next = n2
n2.next = n3
n3.next = None
n4.next = n5
n5.next = n6
n6.next = None

sol = Solution()
n7 = sol.addTwoNumbers(l1=n1, l2=n4)
