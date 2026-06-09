class Solution:
    def isValid(self, s: str) -> bool:
        # list_parentheses = [["(",")"],["{","}"],["[","]"]]
        # num = 0

        # for i in range(0,len(s)//2):
        #     if [s[i],s[len(s)-(i+1)]] in list_parentheses :
        #         num +=1
            
        # if num == len(s)//2:
        #     return True
        # else:
        #     return False

        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()","").replace("{}","").replace("[]","")

        return s == "" 