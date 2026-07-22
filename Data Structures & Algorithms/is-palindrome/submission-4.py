class Solution:
    def isPalindrome(self, s: str) -> bool:
        original_s = s.lower()
        original = ""
        palindrome = ""
        for char in original_s:
            if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890":
                continue
            original += char
            palindrome = char + palindrome

        if original == palindrome:
            return True

        return False