# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        count = 0
        count_ptr = head
        while count_ptr:
            count += 1
            count_ptr = count_ptr.next
        batch_count = count // k
        sentinel = ListNode()
        sentinel.next = head

        ptr = head
        prev_tail = sentinel
        next_batch_start = None
        while batch_count > 0:
            array = []
            for i in range(k):
                if i == k - 1:
                    next_batch_start = ptr.next
                array.append(ptr)
                ptr = ptr.next
            partial_sentinel = ListNode()
            new_ptr = partial_sentinel

            this_batch_start = array[-1]
            prev_tail.next = this_batch_start
            while array:
                new_ptr.next = array.pop()
                new_ptr = new_ptr.next
            prev_tail = new_ptr
            new_ptr.next = next_batch_start
            ptr = next_batch_start

            batch_count -= 1
        return sentinel.next