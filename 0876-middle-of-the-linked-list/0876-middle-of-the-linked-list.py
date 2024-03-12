# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        fast = head
        slow = head
        while fast is not None:
            fast=fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
        return slow
        