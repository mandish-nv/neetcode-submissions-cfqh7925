# from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[]]
        
        if len(strs) == 1:
            return [strs]

        dictionary_main = {}
        dictionary_sub = {}

        for word in strs:
            for letter in word:
                dictionary_sub[letter] = dictionary_sub.get(letter, 0) + 1
            dictionary_main[word] = dictionary_sub
            dictionary_sub = {}

        final = []

        for idx_i, i in enumerate(strs):
            same = []
            # for ind_list in final:
            #     if i in ind_list:
            #         continue
            exists = any(i in ind_list for ind_list in final)
            if exists:
                continue
            same.append(i)
            for idx_j, j in enumerate(strs):
                if idx_i == idx_j:
                    continue
                
                if dictionary_main[i] == dictionary_main[j]:
                    same.append(j)

            final.append(same)

        return final
                








