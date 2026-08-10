# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ptr = dummy
        for _ in range(n):
            ptr = ptr.next

        qtr = dummy
        while ptr.next:
            ptr = ptr.next
            qtr = qtr.next
        
        print(qtr.val)

        if qtr.next:
            qtr.next = qtr.next.next

        return dummy.next