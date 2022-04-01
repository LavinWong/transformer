class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        if len(s) % 2 != 0:
            return False

        
        # count if open brackets == closing brackets
        cnt_opens = 0
        cnt_closes = 0
        
        # stack for finding matching brackets 
        stack = []
        
        # brackets map 
        brackets = {"}":"{", "]":"[",")":"("}
        
        for c in s:
            
            # append element to stack if it is a open bracket
            if c in ["[","{","("]: 
                cnt_opens+= 1  
                stack.append(c)
                
            # if element is a closing bracket
            # pop from the stack the latest element appended to it 
            # check if they match  
            elif c in ["]","}",")"]:
                cnt_closes+= 1
                if stack and brackets[c] != stack.pop():
                    return False 
                           
        return len(stack) == 0 and cnt_closes == cnt_opens
        
                
