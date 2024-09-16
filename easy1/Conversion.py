class Conversion:
    def reverseInt(self, x: int) -> int:
        negative = 1
        if x<0: 
            negative = -1
            x=x*negative
        s = str(x)
        sr = ""
        for i in range(len(s)-1,-1,-1):
            sr+=s[i]
        print("[string reversed:]", sr, " = ", (int(sr) * negative))
        r = int(sr) * negative
        if -pow(2,31) <= r <= pow(2,31)-1: return r
        return 0
    
