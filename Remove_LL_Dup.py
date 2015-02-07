# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head: return None
        dummy = ListNode(-1)
        runner, data, tail = head.next, head.data, dummy
        
        while runner:
            if runner.val == data:
                runner = runner.next
            
            # last node 
            elif not runner.next:
                tail.next = runner 
                
            elif runner.next.val != runner.val:
                data = runner.next.val
                tail.next = runner
                tail = tail.next
                runner = runner.next 
        return dummy.next 
            
                
                
                
              
            
