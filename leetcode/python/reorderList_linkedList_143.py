# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    from typing import Optional


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # use slow/fast to identify midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list
        curr = slow.next
        prev = slow.next = None

        # reverse right half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        # merge list
        head2 = prev
        while head2:
            temp1, temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp1
            head, head2 = temp1, temp2
