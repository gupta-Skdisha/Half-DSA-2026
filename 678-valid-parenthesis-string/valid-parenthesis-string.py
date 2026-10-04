class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin represents the minimum possible open brackets
        # cmax represents the maximum possible open brackets
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                # If '*' is ')', cmin decreases
                # If '*' is '(', cmax increases
                cmin -= 1
                cmax += 1
            
            # If cmax is negative, there are too many ')' brackets 
            # even if we converted all '*' into '('
            if cmax < 0:
                return False
            
            # cmin cannot be less than 0 because we can choose 
            # to treat '*' as empty strings or '(' instead of ')'
            if cmin < 0:
                cmin = 0
                
        # If cmin is 0, it means all open brackets could be validly closed
        return cmin == 0
