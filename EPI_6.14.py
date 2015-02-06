# Next Permutation 
# Kth Permutation
# Previous Permutation 

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) < 2: return num
        # [1, 3, 5, 0, 4, 3]
        pre_tail = len(num) - 2
        while pre_tail >= 0 and num[pre_tail] >= num[pre_tail + 1]: pre_tail -= 1 
        if pre_tail == -1: 
            num.reverse()
            return num 
        # swap 
        runner = len(num) - 1
        while runner > pre_tail:
            if num[runner] > num[pre_tail]:
                num[pre_tail], num[runner] = num[runner], num[pre_tail]
                break
            runner -= 1 
        num[pre_tail + 1:] = num[len(num) - 1: pre_tail:-1]
        return num 
        
        
        
