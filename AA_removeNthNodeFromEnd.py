# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        fast = head
        for i in range(n):
            fast = fast.next
        
        slow = head
        prev = None
        
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev == None:
            return head.next
        else:
            prev.next = slow.next
        
        return head
        
