"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return None
        curr = head

        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        
        curr = head
        copy = head.next
        ans = head.next

        while curr:
            curr.next = curr.next.next if curr.next else None
            copy.next = copy.next.next if copy.next else None

            copy = copy.next
            curr = curr.next

        return ans



    