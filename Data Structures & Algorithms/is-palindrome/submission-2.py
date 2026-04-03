import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        inverse = ""
        original = ""

        for char in s:
            if char in string.ascii_lowercase or char in string.ascii_uppercase or char in "0123456789":
                inverse = char + inverse
                original = original + char
        print(original)
        print(inverse)
        if original.lower() == inverse.lower():
            return True

        return False