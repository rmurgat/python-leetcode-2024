class NumbersBundle:

    def isHappy(self, n: int) -> bool:
        totals = []
        suma = 0
        while n != 1:
            splitted = list(str(n))
            total = 0
            for d in splitted:
                total = total + pow(int(d), 2)
            if total in totals:
                return False
            totals.append(total)
            n = total

        return True  
    
    def isPowerOfTwo_1(self, n: int) -> bool:
        while n/2 != 1:
           n = n / 2
           if n % 2 != 0:
               return False
        return True
    
    def isPowerOfTwo_2(self, n: int) -> bool:
        return n!=0 and (n-1 & n) == 0     