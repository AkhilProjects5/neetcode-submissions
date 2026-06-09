
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        # s = ''.join(i for i in s if i.isalnum())
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False
        
        # ----------------------------

        i,j = 0,len(s)-1
        while i < j :
            print(i,j)
            while i<j and s[i].isalnum() == False:
                # print(s[i])
                i +=1
            while j> i and s[j].isalnum() == False:
                # print(s[j])
                j -=1

            if s[i] != s[j]:
                return False
            
            i +=1
            j -=1
            
        return True