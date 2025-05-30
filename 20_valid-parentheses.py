class Solution:
    def isValid(self, s: str) -> bool:
        stack=[0]*len(s)
        top=-1
        for char in s:
            if char=='('or char=='{'or char=='[':
                top+=1
                stack[top]=char

            else:
                if top==-1:
                    return False
                if (char==')'and stack[top]!='('or char=='}' and stack[top]!='{'or char==']'and stack[top]!='['):
                    return False

                top-=1

        if top==-1:
            return True
        else:
            return False                

        
