# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util import * 

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head: return None
        if not head.next: return head 
        dummy = ListNode(-1)
        runner, tail = head, dummy
        
        while runner.next:
            print runner, runner.next
            if runner.val == runner.next.val:
                runner = runner.next 
            elif not runner.next.next:
                tail.next = runner.next 
            elif runner.next.next.val == runner.next.val:
                runner = runner.next.next
            else:
                tail.next = runner.next 
                tail = tail.next 
        print dummy.next
        return dummy.next 
            
                
                
                
a = Solution()           
            
            
if __name__ == '__main__':
    values = [1, 2, 3, 3, 3, 4, 5, 5, 6]
    l = createLinkedList(values)
    printLinkedList(l)      
    head = a.deleteDuplicates(l)
    printLinkedList(head)

            
                
                
              
            
