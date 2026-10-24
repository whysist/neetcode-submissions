# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        curr=head
        def gcd(a,b):
            return a if b==0 else gcd(b,a%b)

        while curr.next:
            curVal=curr.val
            nextNode=curr.next
            nextVal=nextNode.val
            gcdVal=gcd(max(curVal,nextVal),min(curVal,nextVal))
            curr.next=ListNode(val=gcdVal,next=nextNode)
            curr=nextNode
        return head


        