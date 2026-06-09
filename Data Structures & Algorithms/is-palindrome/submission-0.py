
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower().replace(" ",''))
        s = ''.join(i for i in s if i.isalnum())
        print(s)
        print(s[::-1])
        if s == s[::-1]:
            return True
        else:
            return False
        