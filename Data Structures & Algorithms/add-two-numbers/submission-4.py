# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head=dummy
        h1,h2=l1,l2
        rem=0
        while h1 and h2:
            val=((h1.val+h2.val)%10)+rem
            rem=(h1.val+h2.val)//10
            head.next=ListNode(val)
            # print(head.next.val)
            head=head.next
            h1=h1.next
            h2=h2.next
        while h1:
            head.next=ListNode((h1.val+rem)%10)
            rem=(h1.val+rem)//10
            head=head.next
            h1=h1.next
        while h2:
            head.next=ListNode((h2.val+rem)%10)
            rem=(h2.val+rem)//10
            head=head.next
            h2=h2.next
        

        if rem:
            head.next=ListNode(rem)
        return dummy.next


