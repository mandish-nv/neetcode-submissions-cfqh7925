class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict = {}

        for s in strs:
            dicts = {}
            for char in s:
                dicts[char] = dicts.get(char, 0) + 1
            
            main_dict[s] = dicts

        final = []
        seen = []
        for i in range(len(strs)):
            common = []
            if strs[i] not in seen:
                seen.append(strs[i])
                common.append(strs[i])
                for j in range(i+1, len(strs)):
                    if main_dict[strs[i]] == main_dict[strs[j]]:
                        common.append(strs[j])
                        seen.append(strs[j])
                final.append(common)

        return final

        

