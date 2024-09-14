class StringUtils:

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


