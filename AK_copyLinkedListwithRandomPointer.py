"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        
        # step - 1, insert the nodes between linkedlist
        
        if not head:
            return head
        
        curr = head
        while curr:
            nxt = curr.next
            new_node = Node(curr.val)
            new_node.next = nxt
            curr.next = new_node
            curr = nxt
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        q = dummy = Node(0)
        dummy.next = head.next
        
        p = head
        q = q.next
        
        while q and q.next and q.next.next:
            p.next = p.next.next
            q.next = q.next.next
            p = p.next
            q = q.next
        
        p.next = None
        
        # ptr = dummy.next
        # while ptr:
            # print(ptr.val)
            # ptr = ptr.next
        
        return dummy.next
