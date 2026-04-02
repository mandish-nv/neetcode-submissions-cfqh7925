class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = strs[0]
        for s in strs[1:]:
            result = result + "." + s
        return (result + ".")

    def decode(self, s: str) -> List[str]:
        result = []
        word = ""
        for strs in s:
            if strs != ".":
                word = word + strs
            else:
                result.append(word)
                word = ""
        
        return result

