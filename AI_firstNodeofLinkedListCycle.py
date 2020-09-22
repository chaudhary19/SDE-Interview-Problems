# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        slow = fast = head
        flag = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                flag = 1    # cycle is present
                break
        
        if flag == 0:
            return None
        
        fast = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        
