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