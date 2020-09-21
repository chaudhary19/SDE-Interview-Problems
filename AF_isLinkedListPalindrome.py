# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        
        if not head or not head.next:
            return True
        
        length, ptr = 0, head
        while ptr:
            length += 1
            ptr = ptr.next
        
        
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        l1 = head
        l2 = slow
        prev.next = None
        
        if length & 1:
            l2 = l2.next
        
        # reverse the second list
        
        curr = l2
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l2 = prev
        
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l2 = l2.next
            l1 = l1.next
        
        return True
