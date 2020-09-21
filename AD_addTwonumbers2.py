# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        stack1, stack2 = [], []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        dummy = curr = ListNode(0)
        
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            remainder = carry % 10
            carry = carry // 10
            
            curr.next = ListNode(remainder)
            curr = curr.next
        
        dummy = dummy.next
        curr = dummy
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
