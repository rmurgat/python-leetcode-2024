from ntpath import join
from typing import List

class LongestSubstrig:

    def ListtoString(self, lst:list)->str:
        r = ""
        for c in lst:
            r+=c
        return r
    
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        if s=="": return 0
        chars = list(s)
        maxlength = 1
        i = 0
        while i<len(chars):
            j = i + 1
            while j<len(chars):
                if chars[j] in chars[i:j]:
                    j=len(chars)
                else:
                    mystr = self.ListtoString(chars[i:(j+1)])
                    maxlength = max(maxlength,len(mystr))
                j+=1
            i+=1
        return maxlength   
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        prefixes = dict()
        for s in strs:
            pre = ""
            for c in s:
                pre+=c
                if prefixes.get(pre):
                    freq = prefixes[pre]+1
                    prefixes.update({pre: freq})
                else:
                    prefixes.update({pre: 1})
        longest = ""
        for pre in prefixes:
            if len(strs) == prefixes[pre]:
                if len(pre) > len(longest):
                    longest = pre
        return longest        
