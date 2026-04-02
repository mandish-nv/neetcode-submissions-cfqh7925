from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        
        for s_char in s:
            s_dict[s_char] = s_dict.get(s_char,0)+1

        for t_char in t:
            t_dict[t_char] = t_dict.get(t_char,0)+1

        if s_dict == t_dict:
            return True
        
        return False