from typing import List


class StringBundle:

    def myAtoi(self, s: str) -> int:
        negative = 1
        i = 0
        s = s.lstrip()
        #while s[i]==' ': i+=1
        if s=="": return 0

        if s[i] == '-':  
            negative = -1
            i+=1
        else:
            if s[i] == '+':  i+=1
        m = i
        while i<len(s):
            print(ord(s[i]), ", ")
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                break
            i+=1
        if m==i: return 0
        print("m:",m," i:",i," num: ", s[m:i] )
        r = int(s[m:i])*negative
        if -pow(2,31) < r < pow(2,31)-1: return r
        return 0
    
    def isValidParentheses(self, s: str) -> bool:
        s = s.strip()
        if s=="": return False
        opening = " ({["
        closing = " )}]"
        stack = []
        for c in s:
            idxO = opening.find(c)
            if idxO > 0 :
                stack.append(c)
            else:
                if len(stack) > 0:
                    idxC = closing.find(c)
                    if stack[-1] == opening[idxC]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not len(stack)>0
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle): return -1
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                j=i
                found = True
                for x in range(0,len(needle)):
                    if needle[x]!=haystack[j]:
                        found=False
                    if j==len(haystack)-1 and x<len(needle)-1: 
                        found = False
                        break
                    j+=1
                if found: 
                    return i
        return -1

    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        i = len(s)-1
        counter = 0
        while s[i]!=' ' and i>=0 : 
            counter+=1
            i-=1
        return counter
    
    def addBinary(self, a: str, b: str) -> str:
        maxlength = max(len(a),len(b))
        a = a.zfill(maxlength)
        b = b.zfill(maxlength)
        carry = 0
        res =""
        for i in range(maxlength-1,-1,-1):
            r = carry
            r += 1 if a[i]=='1' else 0
            r += 1 if b[i]=='1' else 0
            res = ('0' if r==0 or r==2 else '1') + res
            carry = 0 if r<2 else 1
        if carry:
            res = "1" + res
        return res

        
    def generateParenthesis(self, n: int) -> List[str]:

        return []


