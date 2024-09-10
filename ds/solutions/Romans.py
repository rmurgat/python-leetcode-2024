class Romans:
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    #my algo, not optimized
    def romanToInt_1(self, s:str)->int:
        res = 0
        lst = list(s)
        i = len(lst)-1
        while i>=0 :
            val = self.roman[lst[i]]
            if i>0 :
                if lst[i-1] == "I":
                    if lst[i]=="V" or lst[i]=="X": 
                        val -= self.roman[lst[i-1]]
                        i-=1
                if lst[i-1] == "X":
                    if lst[i]=="L" or lst[i]=="C": 
                        val -= self.roman[lst[i-1]]
                        i-=1
                if lst[i-1]=="C":
                    if lst[i]=="D" or lst[i]=="M":
                        val -= self.roman[lst[i-1]]
                        i-=1
            res = res + val
            i-=1
        return res
    
    # algo super short using while 
    def romanToInt_2(self, s:str)->int:
        res = 0
        i = len(s)-1
        while i>=0:
            if i<len(s)-1 and self.roman[s[i]]<self.roman[s[i+1]]:
                res-=self.roman[s[i]]
            else:
                res+=self.roman[s[i]] 
            i-=1
        return res

    # algo short using for
    def romanToInt_3(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i<len(s)-1 and self.roman[s[i]]<self.roman[s[i+1]]:
                res-=self.roman[s[i]]
            else:
                res+=self.roman[s[i]]
        return res
