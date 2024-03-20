# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        curr = list1
        while count < a-1:
            curr = curr.next
            count += 1
        # now curr is at a-1, save it
        a_minus_1 = curr

        while count < b+1:
            curr = curr.next
            count += 1
        # now curr is at b+1
        b_plus_1 = curr

        # connect a-1 to 0
        a_minus_1.next = list2

        # connect m-1 to b+1
        curr2 = list2
        while curr2.next != None:
            curr2 = curr2.next
        # now curr2 is at the last node
        curr2.next = b_plus_1

        return list1