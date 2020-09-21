# Definition for singly-linked list.

# Iterative solution----------------------------------------

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        
        prev = nxt = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
# Recursive solution ------------------------------------------

# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next
        
class Solution(object):
    
    def reverseList(self, head):
        
        return self._reverseList(head, None)
    
    def _reverseList(self, curr, prev):
        
        if not curr:
            return prev
        
        temp = curr.next
        curr.next = prev
        return self._reverseList(temp, curr)
