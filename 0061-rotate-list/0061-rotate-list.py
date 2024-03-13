# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        size = 1
        while curr.next is not None:
            curr = curr.next
            size += 1

        curr.next = head

        i = size - (k % size)

        while i > 1:
            head = head.next
            i -= 1

        curr = head.next
        head.next = None
        return curr
        