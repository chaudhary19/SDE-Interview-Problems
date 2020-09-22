# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        if not head:
            return head
        
        length = 0
        ptr = head
        
        while ptr:
            length += 1
            ptr = ptr.next
        
        k %= length
        
        if k == 0:
            return head
        
        fast = head
        for i in range(k):
            fast = fast.next
        
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head
        
        
