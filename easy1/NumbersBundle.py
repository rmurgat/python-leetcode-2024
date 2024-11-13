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
    
    def divide_1(self, dividend: int, divisor: int) -> int:
        ans = []
        signe = 1
        
        if divisor < 0:
            signe = -1
            ans.append("-")
            divisor = -divisor
        if dividend < 0 :
            signe = -1 * signe
            dividend = -dividend  

        if divisor == 1: return dividend * signe
        suma = divisor
        floor = 1
        left = 0

        while suma < dividend:
            left = dividend - suma
            suma = suma + divisor
            floor += 1

        if suma == dividend: 
            return floor*signe 
        else:
            ans.append(floor-1)
            times = 0
            while times < 3:
                dividend1 = left
                divisor1 = float("0."+("0"*times) + str(divisor))
                fractions = 1
                suma = divisor1
                while suma < dividend1:
                    left = dividend1 - suma
                    suma = suma + divisor1
                    fractions += 1 
                if suma == dividend1:
                    ans.append(fractions)
                    break
                else:
                    ans.append(fractions-1)
                times +=1
        print(ans)
        return int((floor-1)*signe)