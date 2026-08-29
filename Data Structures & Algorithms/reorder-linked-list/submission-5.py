from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next :
            return 
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.val)

        l1=head
        
        
        curr=slow.next
        slow.next=None
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        l2=prev
        while l2:
            next1=l1.next
            next2=l2.next
            l1.next=l2
            l2.next=next1
            l1=next1
            l2=next2

        