# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev = None
        curr = slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # now prev is the head of the second list
        slow.next = None

        # merge the two list
        h1, h2 = head, prev
        while h2:
            h1next = h1.next
            h1.next = h2
            h2next = h2.next
            h2.next = h1next
            h1 = h1next
            h2 = h2next

        
        