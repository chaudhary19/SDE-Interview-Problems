# According to geeksforgeeks, reverse all k groups and also reverse the remaining part

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        
        dummy = jump = ListNode(0)
        l = r = dummy.next = head
        
        while True:
            
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            
            if count == k:
                
                curr = l
                prev = r
                
                for i in range(k):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                
                jump.next = prev
                jump = l
                l = r
            
            else:     # reverse this remaining part also, inspired from gfg
                
                prev = None
                curr = l
                
                while curr:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                
                jump.next = prev
                return dummy.next
                
 # according to leetcode, reverse only complete K length groups and left the remaining one....
 
 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        
        dummy = jump = ListNode(0)
        l = r = dummy.next = head
        
        while True:

            count = 0
            while r and count < k:
                count += 1
                r = r.next
            
            if count == k:
                curr = l
                prev = r
                
                for i in range(k):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                
                jump.next = prev
                jump = l
                l = r
            
            else:
                return dummy.next
