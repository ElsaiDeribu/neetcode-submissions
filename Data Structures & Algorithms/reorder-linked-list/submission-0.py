# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find half way
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # reverse second half
        prev = None
        curr = slow

        while curr:
            temp = curr.next

            curr.next = prev
            prev = curr
            curr = temp

        
        # interleave
        left, right = head, prev

        while right.next:

            temp = left.next

            left.next = right
            right = right.next
            left.next.next = temp
            left = temp



















        