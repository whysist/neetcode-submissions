# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        thing=[]
        curr=head
        prev=None
        while curr:
            thing.append(curr.val)
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        c=prev
        back=[]
        while c:
            back.append(c.val)
            c=c.next
        return thing==back


        
        