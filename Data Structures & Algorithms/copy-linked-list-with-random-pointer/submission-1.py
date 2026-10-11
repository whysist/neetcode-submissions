from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        # vis=defaultdict()
        copy_map=defaultdict()
        cur=head
        while cur:
            copy_map[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy=copy_map[cur]
            copy.next=copy_map[cur.next] if cur.next else None
            copy.random=copy_map[cur.random] if cur.random else None
            cur=cur.next
        return copy_map[head]