# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# [1, 2, 3, 4, 5] ----> 3    (odd case)
# [1, 2, 3, 4, 5, 6] ----> 4 (even case)
