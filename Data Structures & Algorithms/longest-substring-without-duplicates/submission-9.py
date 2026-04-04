class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        temp = ""
        for idx, char in enumerate(s):
            if char not in temp:
                temp = temp + char
            else: # duplicate case
                temp_len = len(temp)
                longest_len = len(longest)
                if temp_len > longest_len:
                    longest = temp
                same = temp.index(char)
                temp = temp[same + 1:] + char

        if len(longest) < len(temp):
            return len(temp)

        return len(longest)