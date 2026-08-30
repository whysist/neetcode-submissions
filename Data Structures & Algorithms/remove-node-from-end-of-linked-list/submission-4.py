# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n==1:
            return None
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        if n==count:
            return head.next
        N=count-n
        c=head
        for _ in range(N-1):
            c=c.next
        # print(c.val)
        temp=c.next
        c.next=temp.next
        temp.next=None
        del temp
        return head