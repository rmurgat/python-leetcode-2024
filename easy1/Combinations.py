class Combinations:

    def combinations(self, comb: list, tmp: list, n: int):
        sum=0
        for x in tmp: sum += x
        if sum > n: return
        if sum == n: 
            comb.append(tmp.copy())
            return
        
        tmp.append(1)
        self.combinations(comb, tmp, n)
        tmp.pop()

        tmp.append(2)
        self.combinations(comb, tmp, n)
        tmp.pop()

    def climbStairs(self, n: int) -> int:
        comb = []
        self.combinations(comb, [], n)
        #print("combinations:", comb)
        return len(comb)
