class Palindrome:

    def isPalindrome(s:str) -> bool:
        i = 0
        j = len(s)-1
        while (i<j):
            if s[i]!=s[j]: 
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
        
        


