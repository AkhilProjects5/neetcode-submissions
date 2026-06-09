class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # if sorted_s == sorted_t:
        #     return True
        
        # return False

        # ---------------------------------

        # dict_s = {}
        # dict_t = {}
        # for letter in s :
        #     if letter not in dict_s.keys():
        #         dict_s[letter] = 1
        #     else:
        #         dict_s[letter] = dict_s[letter]+1

        # for letter in t :
        #     if letter not in dict_t.keys():
        #         dict_t[letter] = 1
        #     else:
        #         dict_t[letter] = dict_t[letter]+1
        
        # if dict_s.keys() == dict_t.keys():
        #     for key in dict_s.keys():
        #         if dict_s[key] == dict_t[key]:
        #             return True
        
        # return False

        # ---------------------------------------

        # dict_s = {}
        
        # for letter in s :
        #     if letter not in dict_s.keys():
        #         dict_s[letter] = 1
        #     else:
        #         dict_s[letter] = dict_s[letter]+1
        
        # for letter in t :
        #     if letter not in dict_s.keys():
        #         return False
        #     else:
        #         dict_s[letter] = dict_s[letter]-1
        #         if dict_s[letter] == 0 :
        #             del dict_s[letter]
        
        # if len(dict_s.keys()) != 0 :
        #     return False

        # return True

        # -----------------------------------------

        if len(s) != len(t):
            return False
        count = [0]*26

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] +=1
            count [ord(t[i]) - ord("a")] -=1

        for val in count:
            if val !=0:
                return False

        return True

        # -----------------------------------------


                




        

