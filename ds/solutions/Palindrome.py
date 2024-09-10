class Palindrome:

    def isPalindrome(self, cadena:str) -> bool:
        x = list(cadena)
        i = 0
        j = len(x)-1
        while (i!=j):
            print(x[i],"!=", x[j],"(i,j)",i,j)
            if x[i]!=x[j]: 
                return False
            i+=1
            j-=1

        return True


    def isPalindromeInt(self, num:int) -> bool:
        if num<0: 
            return False
        snum = str(num)
        return self.isPalindrome(snum)

