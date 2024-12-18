from typing import List


class StringBundle:

    def isPalindrome(self, s:str) -> bool:
        i = 0
        j = len(s)-1
        while (i<j):
            if s[i]!=s[j]: 
                return False
            i+=1
            j-=1
        return True
    
    def isPalindromeAlpha(self, s:str) -> bool:
        tmp = ""
        s = s.lower()
        for c in s:
            if c.isalpha() or c.isnumeric(): tmp+=c
        print ("tmp:"+tmp)
        if not tmp: return True
        i = 0
        j = len(tmp)-1
        while (i<j):
            if tmp[i]!=tmp[j]: 
                return False
            i+=1
            j-=1
        return True


    def isPalindromeInt(self, num:int) -> bool:
        if num<0: 
            return False
        snum = str(num)
        return self.isPalindrome(snum)
    
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s): return s
        longest = 0
        longstr = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                    news = s[i:j] 
                    if self.isPalindrome(news):
                        if len(news) > longest:
                            longest = len(news)
                            longstr = news  
        return longstr
        
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

        
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            remainder = columnNumber % 26
            res+=chr(int(remainder)+ord('A'))
            columnNumber = int(columnNumber / 26)
        return res[::-1]

    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        power = len(columnTitle)-1
        for ch in columnTitle:
            res += (ord(ch)-64) * (26**power) 
            power -= 1
        return res 

    def convertZigZag(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        re = ""
        matrix = [[' '] * len(s) for _ in range(numRows)]
        col = 0
        row = 0
        forward = True
        
        for car in s:
            print ("i,j:[",row,",",col,"]=",car)
            matrix[row][col] = car
            if forward:
                if row == numRows - 1:
                    row = row - 1
                    col = col + 1
                    forward = False
                else:
                    row = row + 1
            else:
                if row == 0:
                    row = 1
                    forward = True
                else:
                    row = row - 1
                    col = col + 1

        for row in matrix:
            print(row)

        for row in matrix:
            for car in row:
                if car!=' ': re = re + car

        return re
    
    def countAndSay(self, n: int) -> str:
        res = ""
        def RLE(s:str, count:int) -> str:
            ans = []
            l = len(s)
            count = 0
            if l==0: return "1"
            c = s[l-1]
            for i in range (l-1,-1,-1):
                if c!=s[i]:
                    ans.append(str(count)+c)
                    c = s[i]
                    count = 0
                count = count + 1
            ans.append(str(count)+c)
            return "".join(ans[::-1])
        while n>0:
            res = RLE(res,0)
            n -=1
        return res

    # https://leetcode.com/problems/multiply-strings/
    def multiply(self, num1: str, num2: str) -> str:
        total = "0"

        def sumStrings(num1:str, num2:str) -> str:
            l = max(len(num1),len(num2))
            num1 = num1.zfill(l)
            num2 = num2.zfill(l)
            res = ""
            left = 0
            for i in range (len(num1)-1,-1,-1):
                suma = int(num1[i]) + int(num2[i]) + left
                if suma > 9: 
                    left = 1
                    suma = suma - 10
                else:
                    left = 0
                res = res + str(suma)
            return ("1" if left>0 else "") + res[::-1]

        zeroi = 0    
        for i in range (len(num1)-1,-1,-1):
            suma = ""
            zeroj = 0
            for j in range (len(num2)-1,-1,-1):
                smult = str(int(num1[i])*int(num2[j])) + ("0"*(zeroi+zeroj))
                suma = sumStrings(suma, smult)
                zeroj = zeroj + 1
            total = sumStrings(total, suma)
            zeroi = zeroi + 1
            
        total = total.lstrip('0')

        return "0" if not total else total
    
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for c in s:
            cnt = d.get(c,0)
            if cnt==0:
                d[c]=1
            else:
                d[c]=d[c]+1
        for c in t:
            cnt = d.get(c,None)
            if cnt:
                d[c]=d[c]-1
            else:
                return False
        dif = [y for x,y in d.items() if y!=0]
        return False if len(dif) > 0 else True