
from typing import List


class IntervalBundle1:
    
    # https://leetcode.com/problems/merge-intervals/
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        L = len(intervals)
        toadd = intervals[0]
        last = intervals[0]
        ans = []
        for i in range(L):
            cur = intervals[i]
            if cur[0] > toadd[1]:
                toadd[1] = max(last[1], toadd[1])
                ans.append(toadd)
                toadd = cur
            else:
                toadd[1] = max(toadd[1], cur[1])
            last = cur
        ans.append(toadd)

        return ans


    # https://leetcode.com/problems/insert-interval
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        L = len(intervals)
        intervals.sort(key=lambda x: x[0])
        maxi = 0
        print ("original sorted: ", intervals)

        def maxOverlaping(start) -> int:
            counter = 1
            last = intervals[start]
            for i in range (start, L):
                cur = intervals[i]
                if cur[0]==last[1]:
                    counter+=1
                    last = cur
            return counter

        for i in range (0, L):
            maxi = max(maxi, maxOverlaping(i))

        return L - maxi

    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass


